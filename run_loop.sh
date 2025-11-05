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
