#!/usr/bin/env python3
"""
🌙 Moon Dev's Strategy Demo
Demonstração das 5 estratégias de trading em ação
"""

from termcolor import cprint
import time
import random

def print_header():
    """Print demo header"""
    cprint("=" * 80, "cyan")
    cprint("🌙 MOON DEV AI TRADING AGENTS - STRATEGY DEMO 🚀", "yellow", attrs=["bold"])
    cprint("=" * 80, "cyan")
    print()

def simulate_rsi_volume_strategy():
    """Simulate RSI + Volume Strategy"""
    cprint("📊 Estratégia 1: RSI + Volume Surge", "cyan", attrs=["bold"])
    print("   Tipo: Mean Reversion (Reversão à Média)")
    print("   Indicadores: RSI (14), Volume 1.5x")
    print()

    time.sleep(0.5)

    # Simulate token analysis
    cprint("🔍 Analyzing 9BB6NFE... with RSI + Volume strategy", "cyan")
    time.sleep(0.3)

    # Simulate data
    rsi = round(random.uniform(25, 35), 1)
    volume_ratio = round(random.uniform(1.5, 2.5), 1)
    signal_strength = round(random.uniform(0.75, 0.95), 2)
    price = round(random.uniform(0.0001, 0.001), 6)

    cprint(f"🟢 BUY Signal for 9BB6NFE...: RSI={rsi}, Vol={volume_ratio}x, Strength={signal_strength}", "green")
    cprint(f"   Current Price: ${price}", "white")
    cprint(f"   Reasoning: RSI oversold ({rsi}) with {volume_ratio}x volume surge", "yellow")
    print()
    time.sleep(1)

def simulate_bollinger_strategy():
    """Simulate Bollinger Bands Strategy"""
    cprint("📊 Estratégia 2: Bollinger Bands Mean Reversion", "cyan", attrs=["bold"])
    print("   Tipo: Mean Reversion (Reversão à Média)")
    print("   Indicadores: BB (20,2), RSI")
    print()

    time.sleep(0.5)

    cprint("🔍 Analyzing 9BB6NFE... with Bollinger Mean Reversion strategy", "cyan")
    time.sleep(0.3)

    current_price = round(random.uniform(0.0001, 0.001), 6)
    bb_lower = current_price * 0.98
    rsi = round(random.uniform(30, 38), 1)
    signal_strength = round(random.uniform(0.70, 0.90), 2)

    cprint(f"🟢 BUY Signal for 9BB6NFE...: Price at lower BB, RSI={rsi}, Strength={signal_strength}", "green")
    cprint(f"   Price touching lower BB (${current_price:.6f} vs ${bb_lower:.6f})", "white")
    cprint(f"   RSI oversold at {rsi}", "yellow")
    print()
    time.sleep(1)

def simulate_macd_strategy():
    """Simulate MACD Momentum Strategy"""
    cprint("📊 Estratégia 3: MACD Momentum Breakout", "cyan", attrs=["bold"])
    print("   Tipo: Trend Following (Seguidor de Tendência)")
    print("   Indicadores: MACD (12,26,9), Histogram, Volume")
    print()

    time.sleep(0.5)

    cprint("🔍 Analyzing 9BB6NFE... with MACD Momentum strategy", "cyan")
    time.sleep(0.3)

    histogram = round(random.uniform(0.00001, 0.00005), 6)
    volume_ratio = round(random.uniform(1.3, 2.0), 1)
    signal_strength = round(random.uniform(0.80, 0.95), 2)

    cprint(f"🟢 BUY Signal for 9BB6NFE...: MACD Bullish Cross, Hist={histogram:.6f}, Vol={volume_ratio}x, Strength={signal_strength}", "green")
    cprint(f"   Crossover Type: Bullish", "white")
    cprint(f"   Reasoning: Bullish MACD crossover with strong momentum", "yellow")
    print()
    time.sleep(1)

def simulate_confluence_strategy():
    """Simulate Multi-Indicator Confluence Strategy"""
    cprint("📊 Estratégia 4: Multi-Indicator Confluence", "cyan", attrs=["bold"])
    print("   Tipo: High Confidence Signals (Alta Confiança)")
    print("   Indicadores: RSI + MACD + EMA + Volume + Momentum")
    print()

    time.sleep(0.5)

    cprint("🔍 Analyzing 9BB6NFE... with Multi-Indicator Confluence strategy", "cyan")
    time.sleep(0.3)

    confluence_count = random.choice([4, 5])
    aligned = ['RSI oversold', 'MACD bullish', 'EMA bullish', 'Volume surge']
    if confluence_count == 5:
        aligned.append('Price momentum up')

    signal_strength = round(confluence_count / 5, 2)

    cprint(f"🟢 BUY Signal for 9BB6NFE...: {confluence_count}/5 indicators aligned, Strength={signal_strength}", "green")
    cprint(f"   Aligned: {', '.join(aligned)}", "cyan")
    cprint(f"   Reasoning: {confluence_count}/5 bullish indicators aligned", "yellow")
    print()
    time.sleep(1)

def simulate_ema_volume_strategy():
    """Simulate EMA + Volume Strategy"""
    cprint("📊 Estratégia 5: EMA Crossover + Volume", "cyan", attrs=["bold"])
    print("   Tipo: Trend Following (Seguidor de Tendência)")
    print("   Indicadores: Triple EMA (9/21/50), Volume 1.5x")
    print()

    time.sleep(0.5)

    cprint("🔍 Analyzing 9BB6NFE... with EMA + Volume strategy", "cyan")
    time.sleep(0.3)

    ema_fast = round(random.uniform(0.0001, 0.001), 6)
    ema_med = ema_fast * 0.98
    ema_slow = ema_fast * 0.96
    volume_ratio = round(random.uniform(1.5, 2.2), 1)
    signal_strength = round(random.uniform(0.75, 0.92), 2)

    cprint(f"🟢 BUY Signal for 9BB6NFE...: EMA Bullish Cross, Vol={volume_ratio}x, Strength={signal_strength}", "green")
    cprint(f"   EMAs: Fast={ema_fast:.6f} > Med={ema_med:.6f} > Slow={ema_slow:.6f}", "cyan")
    cprint(f"   Reasoning: Bullish EMA cross with strong volume confirmation", "yellow")
    print()
    time.sleep(1)

def simulate_llm_validation():
    """Simulate LLM validation of signals"""
    cprint("=" * 80, "magenta")
    cprint("🤖 CLAUDE LLM VALIDATION", "magenta", attrs=["bold"])
    cprint("=" * 80, "magenta")
    print()

    cprint("📝 Analyzing all signals with Claude AI...", "cyan")
    time.sleep(1)

    signals_found = random.randint(2, 3)
    cprint(f"✅ Found {signals_found} high-confidence signals across strategies", "green")
    print()

    time.sleep(0.5)

    cprint("🔍 Claude Analysis:", "yellow")
    print("   • Multiple strategies agree on bullish sentiment")
    print("   • Volume confirmation is strong across all signals")
    print("   • RSI and MACD show momentum alignment")
    print("   • Risk/Reward ratio: 3.2:1 (favorable)")
    print()

    time.sleep(0.5)

    cprint("⚖️  Risk Management Check:", "yellow")
    print(f"   • Current Position Size: $25 (within limits)")
    print(f"   • Available Cash: $180 (>20% minimum)")
    print(f"   • Max Loss USD: $25 (not breached)")
    print(f"   • Portfolio Exposure: 12% (under 30% max)")
    print()

    time.sleep(0.5)

    cprint("✅ DECISION: EXECUTE BUY", "green", attrs=["bold"])
    cprint("   Confidence: 87%", "green")
    cprint("   Position Size: $25 (based on signal strength 0.87)", "green")
    print()

def show_strategy_summary():
    """Show strategy summary"""
    cprint("=" * 80, "cyan")
    cprint("📊 ESTRATÉGIAS ATIVAS - RESUMO", "yellow", attrs=["bold"])
    cprint("=" * 80, "cyan")
    print()

    strategies = [
        ("1. RSI + Volume Surge", "✅ Active", "green"),
        ("2. Bollinger Mean Reversion", "✅ Active", "green"),
        ("3. MACD Momentum Breakout", "✅ Active", "green"),
        ("4. Multi-Indicator Confluence", "✅ Active", "green"),
        ("5. EMA Crossover + Volume", "✅ Active", "green"),
    ]

    for name, status, color in strategies:
        cprint(f"   {name}: {status}", color)

    print()
    cprint("⚙️  Configuration:", "cyan")
    print("   • Min Confidence: 70%")
    print("   • Position Size: $25")
    print("   • Timeframe: 15m")
    print("   • LLM Validation: Enabled (Claude)")
    print()

def main():
    """Main demo function"""
    try:
        print_header()
        show_strategy_summary()

        time.sleep(1)

        cprint("🚀 Iniciando análise de mercado...", "yellow", attrs=["bold"])
        print()
        time.sleep(1)

        # Run all strategies
        simulate_rsi_volume_strategy()
        simulate_bollinger_strategy()
        simulate_macd_strategy()
        simulate_confluence_strategy()
        simulate_ema_volume_strategy()

        # LLM Validation
        simulate_llm_validation()

        # Final summary
        cprint("=" * 80, "cyan")
        cprint("✅ ANÁLISE COMPLETA", "green", attrs=["bold"])
        cprint("=" * 80, "cyan")
        print()

        cprint("📈 Próximos Passos:", "yellow")
        print("   1. Configure seus tokens em src/config.py")
        print("   2. Execute: python src/agents/strategy_agent.py")
        print("   3. Ou execute todos os agentes: python src/main.py")
        print()

        cprint("💡 Dica:", "cyan")
        print("   As estratégias funcionam em paralelo e se validam mutuamente")
        print("   Quando múltiplas estratégias concordam, a confiança aumenta!")
        print()

        cprint("⚠️  Lembrete:", "yellow")
        print("   Sempre teste em paper trading antes de usar capital real")
        print("   Configure limites de risco apropriados no config.py")
        print()

        cprint("🌙 Moon Dev - Building the future of AI trading! 🚀", "magenta", attrs=["bold"])
        print()

    except KeyboardInterrupt:
        print()
        cprint("\n👋 Demo interrompida pelo usuário", "yellow")
        print()

if __name__ == "__main__":
    main()
