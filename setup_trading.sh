#!/bin/bash

# 🌙 Moon Dev Trading Setup Script
# Automatiza a configuração inicial do sistema de trading

set -e  # Exit on error

echo "================================================================================"
echo "🌙 MOON DEV AI TRADING AGENTS - SETUP AUTOMÁTICO"
echo "================================================================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "ℹ️  $1"
}

# Check if .env exists
echo "📋 Passo 1: Verificando arquivo .env..."
if [ ! -f .env ]; then
    print_warning "Arquivo .env não encontrado. Criando do template..."

    if [ -f .env_example ]; then
        cp .env_example .env
        print_success "Arquivo .env criado de .env_example"
    else
        # Create basic .env
        cat > .env <<EOF
# Moon Dev AI Trading Agents - Environment Variables

# === OBRIGATÓRIO ===
BIRDEYE_API_KEY=your_birdeye_key_here

# === RECOMENDADO ===
ANTHROPIC_KEY=your_anthropic_key_here

# === OPCIONAL ===
COINGECKO_API_KEY=
MOONDEV_API_KEY=

# === TRADING (CUIDADO!) ===
# SOLANA_PRIVATE_KEY=
EOF
        print_success "Arquivo .env básico criado"
    fi

    print_warning "AÇÃO NECESSÁRIA: Edite o arquivo .env e adicione suas API keys"
    print_info "nano .env  # ou use seu editor preferido"
    echo ""
else
    print_success "Arquivo .env encontrado"
fi

# Check for required API keys
echo ""
echo "📋 Passo 2: Verificando API Keys..."

if grep -q "your_birdeye_key_here" .env 2>/dev/null || ! grep -q "BIRDEYE_API_KEY=." .env 2>/dev/null; then
    print_error "BIRDEYE_API_KEY não configurada no .env"
    print_info "Obtenha em: https://birdeye.so/"
    BIRDEYE_OK=false
else
    print_success "BIRDEYE_API_KEY configurada"
    BIRDEYE_OK=true
fi

if grep -q "your_anthropic_key_here" .env 2>/dev/null || ! grep -q "ANTHROPIC_KEY=." .env 2>/dev/null; then
    print_warning "ANTHROPIC_KEY não configurada (recomendada)"
    print_info "Obtenha em: https://console.anthropic.com/"
else
    print_success "ANTHROPIC_KEY configurada"
fi

# Check Python
echo ""
echo "📋 Passo 3: Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    print_success "Python encontrado: $PYTHON_VERSION"
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    print_success "Python encontrado: $PYTHON_VERSION"
    PYTHON_CMD=python
else
    print_error "Python não encontrado!"
    exit 1
fi

# Check/Install dependencies
echo ""
echo "📋 Passo 4: Verificando dependências..."

if [ -f requirements.txt ]; then
    print_info "Instalando dependências (isso pode demorar)..."

    # Try to install
    if $PYTHON_CMD -m pip install -r requirements.txt --quiet 2>/dev/null; then
        print_success "Dependências instaladas com sucesso"
    else
        print_warning "Algumas dependências falharam. Tentando essenciais..."
        $PYTHON_CMD -m pip install termcolor requests python-dotenv pandas numpy --quiet
        print_success "Dependências essenciais instaladas"
    fi
else
    print_warning "requirements.txt não encontrado"
fi

# Test imports
echo ""
echo "📋 Passo 5: Testando importações..."

$PYTHON_CMD -c "
try:
    import termcolor
    print('✅ termcolor OK')
except:
    print('❌ termcolor faltando')

try:
    import requests
    print('✅ requests OK')
except:
    print('❌ requests faltando')

try:
    import pandas
    print('✅ pandas OK')
except:
    print('❌ pandas faltando')

try:
    import numpy
    print('✅ numpy OK')
except:
    print('❌ numpy faltando')

try:
    from dotenv import load_dotenv
    print('✅ python-dotenv OK')
except:
    print('❌ python-dotenv faltando')
" 2>/dev/null

# Check config.py
echo ""
echo "📋 Passo 6: Verificando configuração..."

if [ -f src/config.py ]; then
    if grep -q "ENABLE_STRATEGIES = True" src/config.py; then
        print_success "Estratégias habilitadas em config.py"
    else
        print_warning "Estratégias podem estar desabilitadas em config.py"
    fi

    TOKEN_COUNT=$(grep -c "'" src/config.py | head -1 || echo "0")
    print_info "Tokens configurados em MONITORED_TOKENS"
else
    print_error "src/config.py não encontrado!"
fi

# Create monitoring script
echo ""
echo "📋 Passo 7: Criando scripts úteis..."

# Quick test script
cat > test_connection.py <<'EOF'
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
EOF

chmod +x test_connection.py

print_success "Script de teste criado: test_connection.py"

# Create run script
cat > run_loop.sh <<'EOF'
#!/bin/bash
# Executa estratégias em loop contínuo

echo "🔄 Iniciando loop de trading..."
echo "Pressione Ctrl+C para parar"
echo ""

while true; do
    echo "═══════════════════════════════════════════════════════"
    echo "🌙 $(date '+%Y-%m-%d %H:%M:%S') - Nova análise"
    echo "═══════════════════════════════════════════════════════"

    PYTHONPATH=/home/user/moon-dev-ai-agents python src/agents/strategy_agent.py

    SLEEP_TIME=300  # 5 minutos
    echo ""
    echo "⏳ Aguardando $((SLEEP_TIME/60)) minutos até próxima análise..."
    sleep $SLEEP_TIME
done
EOF

chmod +x run_loop.sh

print_success "Script de loop criado: run_loop.sh"

# Summary
echo ""
echo "================================================================================"
echo "📊 RESUMO DO SETUP"
echo "================================================================================"
echo ""

if [ "$BIRDEYE_OK" = true ]; then
    echo "✅ Sistema pronto para uso!"
    echo ""
    echo "🚀 PRÓXIMOS PASSOS:"
    echo ""
    echo "1️⃣  TESTAR CONEXÃO:"
    echo "   python test_connection.py"
    echo ""
    echo "2️⃣  DEMO COM DADOS SIMULADOS:"
    echo "   python run_strategies_realistic.py"
    echo ""
    echo "3️⃣  MODO PAPER TRADING (sem executar trades):"
    echo "   python src/agents/strategy_agent.py"
    echo ""
    echo "4️⃣  MODO LOOP CONTÍNUO:"
    echo "   ./run_loop.sh"
    echo ""
    echo "📖 DOCUMENTAÇÃO COMPLETA:"
    echo "   cat SETUP_REAL_TIME_TRADING.md"
    echo ""
else
    echo "⚠️  AÇÃO NECESSÁRIA:"
    echo ""
    echo "1️⃣  Configure sua BIRDEYE_API_KEY:"
    echo "   • Obtenha em: https://birdeye.so/"
    echo "   • Edite: nano .env"
    echo "   • Adicione: BIRDEYE_API_KEY=sua_key_aqui"
    echo ""
    echo "2️⃣  Depois execute:"
    echo "   python test_connection.py"
    echo ""
fi

echo "================================================================================"
echo "🌙 Moon Dev - Happy Trading! 🚀"
echo "================================================================================"
