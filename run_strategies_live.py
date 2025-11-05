#!/usr/bin/env python3
"""
🌙 Moon Dev's Strategy Agent Runner
Versão simplificada que roda as estratégias com dados reais
"""

import sys
import os

# Add project to path
sys.path.insert(0, '/home/user/moon-dev-ai-agents')

from termcolor import cprint
import time
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Simple config
MONITORED_TOKENS = ['9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump']
BIRDEYE_API_KEY = os.getenv("BIRDEYE_API_KEY", "demo_key")
BASE_URL = "https://public-api.birdeye.so/defi"

def calculate_rsi(prices, period=14):
    """Calculate RSI manually"""
    deltas = np.diff(prices)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_sma(prices, period):
    """Calculate Simple Moving Average"""
    return np.mean(prices[-period:])

def calculate_ema(prices, period):
    """Calculate Exponential Moving Average"""
    multiplier = 2 / (period + 1)
    ema = prices[0]
    for price in prices[1:]:
        ema = (price - ema) * multiplier + ema
    return ema

def get_token_data(token_address):
    """Fetch token data from BirdEye"""
    try:
        # Get current time
        time_to = int(datetime.now().timestamp())
        time_from = int((datetime.now() - timedelta(days=3)).timestamp())

        url = f"{BASE_URL}/ohlcv?address={token_address}&type=15m&time_from={time_from}&time_to={time_to}"
        headers = {"X-API-KEY": BIRDEYE_API_KEY}

        cprint(f"🔍 Fetching data for {token_address[:8]}...", "cyan")
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json().get('data', {}).get('items', [])
            if not data:
                cprint(f"⚠️  No data returned for {token_address[:8]}", "yellow")
                return None

            df = pd.DataFrame([{
                'time': item['unixTime'],
                'open': item['o'],
                'high': item['h'],
                'low': item['l'],
                'close': item['c'],
                'volume': item['v']
            } for item in data])

            cprint(f"✅ Fetched {len(df)} candles", "green")
            return df
        else:
            cprint(f"❌ API Error: {response.status_code}", "red")
            if response.status_code == 401:
                cprint("⚠️  BIRDEYE_API_KEY may be missing or invalid", "yellow")
            return None

    except Exception as e:
        cprint(f"❌ Error fetching data: {str(e)}", "red")
        return None

def analyze_rsi_volume_strategy(df, token_address):
    """RSI + Volume Strategy Analysis"""
    cprint(f"\n📊 Estratégia 1: RSI + Volume Surge", "cyan", attrs=["bold"])

    if len(df) < 20:
        cprint("⚠️  Insufficient data", "yellow")
        return None

    # Calculate RSI
    rsi = calculate_rsi(df['close'].values)

    # Calculate Volume ratio
    volume_ma = calculate_sma(df['volume'].values, 20)
    current_volume = df['volume'].iloc[-1]
    volume_ratio = current_volume / volume_ma if volume_ma > 0 else 1

    current_price = df['close'].iloc[-1]

    cprint(f"   RSI: {rsi:.1f}", "white")
    cprint(f"   Volume Ratio: {volume_ratio:.2f}x", "white")
    cprint(f"   Current Price: ${current_price:.6f}", "white")

    # Check for signals
    if rsi <= 30 and volume_ratio >= 1.5:
        signal_strength = min(1.0, 0.7 + (30 - rsi) / 100 + (volume_ratio - 1) * 0.1)
        cprint(f"🟢 BUY Signal: RSI oversold with volume surge!", "green")
        cprint(f"   Signal Strength: {signal_strength:.2f}", "green")
        return {'direction': 'BUY', 'strength': signal_strength, 'strategy': 'RSI+Volume'}
    elif rsi >= 70 and volume_ratio >= 1.5:
        signal_strength = min(1.0, 0.7 + (rsi - 70) / 100 + (volume_ratio - 1) * 0.1)
        cprint(f"🔴 SELL Signal: RSI overbought with volume surge!", "red")
        cprint(f"   Signal Strength: {signal_strength:.2f}", "red")
        return {'direction': 'SELL', 'strength': signal_strength, 'strategy': 'RSI+Volume'}
    else:
        cprint(f"⚪ NEUTRAL: No signal (RSI: {rsi:.1f}, Vol: {volume_ratio:.2f}x)", "white")
        return None

def analyze_ema_crossover_strategy(df, token_address):
    """EMA Crossover Strategy Analysis"""
    cprint(f"\n📊 Estratégia 2: EMA Crossover", "cyan", attrs=["bold"])

    if len(df) < 50:
        cprint("⚠️  Insufficient data", "yellow")
        return None

    # Calculate EMAs
    prices = df['close'].values
    ema_9 = calculate_ema(prices, 9)
    ema_21 = calculate_ema(prices, 21)
    ema_50 = calculate_ema(prices, 50)

    # Calculate volume ratio
    volume_ma = calculate_sma(df['volume'].values, 20)
    current_volume = df['volume'].iloc[-1]
    volume_ratio = current_volume / volume_ma if volume_ma > 0 else 1

    current_price = df['close'].iloc[-1]

    cprint(f"   EMA 9: ${ema_9:.6f}", "white")
    cprint(f"   EMA 21: ${ema_21:.6f}", "white")
    cprint(f"   EMA 50: ${ema_50:.6f}", "white")
    cprint(f"   Volume Ratio: {volume_ratio:.2f}x", "white")

    # Check for bullish alignment
    if ema_9 > ema_21 > ema_50 and volume_ratio >= 1.3:
        separation = ((ema_9 - ema_50) / ema_50) * 100
        signal_strength = min(1.0, 0.75 + separation * 0.1 + (volume_ratio - 1) * 0.1)
        cprint(f"🟢 BUY Signal: Bullish EMA alignment with volume!", "green")
        cprint(f"   Signal Strength: {signal_strength:.2f}", "green")
        return {'direction': 'BUY', 'strength': signal_strength, 'strategy': 'EMA Crossover'}
    elif ema_9 < ema_21 < ema_50 and volume_ratio >= 1.3:
        separation = ((ema_50 - ema_9) / ema_50) * 100
        signal_strength = min(1.0, 0.75 + separation * 0.1 + (volume_ratio - 1) * 0.1)
        cprint(f"🔴 SELL Signal: Bearish EMA alignment with volume!", "red")
        cprint(f"   Signal Strength: {signal_strength:.2f}", "red")
        return {'direction': 'SELL', 'strength': signal_strength, 'strategy': 'EMA Crossover'}
    else:
        cprint(f"⚪ NEUTRAL: No clear trend alignment", "white")
        return None

def analyze_sma_strategy(df, token_address):
    """Simple Moving Average Strategy"""
    cprint(f"\n📊 Estratégia 3: SMA Crossover", "cyan", attrs=["bold"])

    if len(df) < 50:
        cprint("⚠️  Insufficient data", "yellow")
        return None

    # Calculate SMAs
    prices = df['close'].values
    sma_20 = calculate_sma(prices, 20)
    sma_50 = calculate_sma(prices, 50)
    current_price = prices[-1]

    cprint(f"   SMA 20: ${sma_20:.6f}", "white")
    cprint(f"   SMA 50: ${sma_50:.6f}", "white")
    cprint(f"   Price: ${current_price:.6f}", "white")

    # Check alignment
    if current_price > sma_20 > sma_50:
        signal_strength = 0.8
        cprint(f"🟢 BUY Signal: Price above both MAs!", "green")
        cprint(f"   Signal Strength: {signal_strength:.2f}", "green")
        return {'direction': 'BUY', 'strength': signal_strength, 'strategy': 'SMA Crossover'}
    elif current_price < sma_20 < sma_50:
        signal_strength = 0.8
        cprint(f"🔴 SELL Signal: Price below both MAs!", "red")
        cprint(f"   Signal Strength: {signal_strength:.2f}", "red")
        return {'direction': 'SELL', 'strength': signal_strength, 'strategy': 'SMA Crossover'}
    else:
        cprint(f"⚪ NEUTRAL: Mixed signals", "white")
        return None

def print_header():
    """Print header"""
    cprint("=" * 80, "cyan")
    cprint("🌙 MOON DEV AI TRADING AGENTS - LIVE EXECUTION 🚀", "yellow", attrs=["bold"])
    cprint("=" * 80, "cyan")
    print()

def main():
    """Main execution"""
    try:
        print_header()

        cprint("⚙️  Configuration:", "cyan")
        print(f"   • Monitored Tokens: {len(MONITORED_TOKENS)}")
        print(f"   • Timeframe: 15m")
        print(f"   • Min Confidence: 0.70")
        print(f"   • API: BirdEye Solana")
        print()

        time.sleep(1)

        for token in MONITORED_TOKENS:
            cprint("=" * 80, "magenta")
            cprint(f"🎯 Analyzing Token: {token[:12]}...{token[-8:]}", "magenta", attrs=["bold"])
            cprint("=" * 80, "magenta")
            print()

            # Fetch data
            df = get_token_data(token)

            if df is None or len(df) < 20:
                cprint("❌ Unable to fetch sufficient data", "red")
                continue

            time.sleep(0.5)

            # Run all strategies
            signals = []

            signal1 = analyze_rsi_volume_strategy(df, token)
            if signal1:
                signals.append(signal1)

            time.sleep(0.3)

            signal2 = analyze_ema_crossover_strategy(df, token)
            if signal2:
                signals.append(signal2)

            time.sleep(0.3)

            signal3 = analyze_sma_strategy(df, token)
            if signal3:
                signals.append(signal3)

            # Summary
            print()
            cprint("=" * 80, "yellow")
            cprint("📊 SIGNAL SUMMARY", "yellow", attrs=["bold"])
            cprint("=" * 80, "yellow")
            print()

            if signals:
                cprint(f"✅ Found {len(signals)} signal(s):", "green")
                for sig in signals:
                    print(f"   • {sig['strategy']}: {sig['direction']} (Strength: {sig['strength']:.2f})")

                # Check consensus
                buy_signals = [s for s in signals if s['direction'] == 'BUY']
                sell_signals = [s for s in signals if s['direction'] == 'SELL']

                print()
                if len(buy_signals) >= 2:
                    avg_strength = sum(s['strength'] for s in buy_signals) / len(buy_signals)
                    cprint(f"🟢 CONSENSUS: BUY ({len(buy_signals)} strategies agree)", "green", attrs=["bold"])
                    cprint(f"   Average Strength: {avg_strength:.2f}", "green")
                elif len(sell_signals) >= 2:
                    avg_strength = sum(s['strength'] for s in sell_signals) / len(sell_signals)
                    cprint(f"🔴 CONSENSUS: SELL ({len(sell_signals)} strategies agree)", "red", attrs=["bold"])
                    cprint(f"   Average Strength: {avg_strength:.2f}", "red")
                else:
                    cprint("⚪ NO CONSENSUS: Mixed signals", "white")
            else:
                cprint("⚪ No signals generated (market neutral)", "white")

            print()

        # Final summary
        cprint("=" * 80, "cyan")
        cprint("✅ ANALYSIS COMPLETE", "green", attrs=["bold"])
        cprint("=" * 80, "cyan")
        print()

        cprint("💡 Next Steps:", "yellow")
        print("   1. Review signals above")
        print("   2. Verify market conditions")
        print("   3. Execute trades manually or enable auto-trading")
        print("   4. Monitor positions and adjust stops")
        print()

        cprint("⚠️  Reminder:", "yellow")
        print("   This is live market data - trade responsibly!")
        print("   Always use proper risk management")
        print()

    except KeyboardInterrupt:
        print()
        cprint("\n👋 Analysis interrupted by user", "yellow")
        print()
    except Exception as e:
        cprint(f"\n❌ Error: {str(e)}", "red")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
