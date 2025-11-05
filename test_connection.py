#!/usr/bin/env python3
"""Quick test script for API connections"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

print("🔍 Testando conexões...\n")

# Test BirdEye
birdeye_key = os.getenv("BIRDEYE_API_KEY")
if birdeye_key and birdeye_key != "your_birdeye_key_here":
    try:
        token = "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
        url = f"https://public-api.birdeye.so/defi/token_overview?address={token}"
        headers = {"X-API-KEY": birdeye_key}
        resp = requests.get(url, headers=headers, timeout=10)

        if resp.status_code == 200:
            print("✅ BirdEye API: FUNCIONANDO")
            data = resp.json().get('data', {})
            price = data.get('price', 0)
            print(f"   Preço do token teste: ${price}")
        else:
            print(f"❌ BirdEye API: ERRO {resp.status_code}")
    except Exception as e:
        print(f"❌ BirdEye API: ERRO - {str(e)}")
else:
    print("⚠️  BirdEye API: KEY NÃO CONFIGURADA")

print()

# Test Anthropic
anthropic_key = os.getenv("ANTHROPIC_KEY")
if anthropic_key and anthropic_key != "your_anthropic_key_here":
    print("✅ Anthropic API: KEY CONFIGURADA")
else:
    print("⚠️  Anthropic API: KEY NÃO CONFIGURADA (opcional)")

print("\n" + "="*50)
print("Setup completo! Próximos passos:")
print("1. Se BirdEye não funcionar, configure a key no .env")
print("2. Execute: python run_strategies_realistic.py")
print("3. Para modo real: python src/agents/strategy_agent.py")
