# 🚀 QUICK START - Comece em 5 Minutos

## O Que Você Precisa Fazer Para Ver Oportunidades de Trade

---

## ⚡ OPÇÃO 1: DEMO RÁPIDO (Sem API Keys)

**Veja as estratégias funcionando AGORA:**

```bash
python run_strategies_realistic.py
```

Isso vai:
- ✅ Simular dados de mercado reais
- ✅ Executar todas as 5 estratégias
- ✅ Mostrar sinais de BUY/SELL
- ✅ Calcular RSI, MACD, Bollinger Bands
- ✅ Validar consenso entre estratégias

**Tempo: 30 segundos** ⏱️

---

## 🔥 OPÇÃO 2: DADOS REAIS (Requer API Key)

### **Passo 1: Obter BirdEye API Key** (2 minutos)

1. Acesse: https://birdeye.so/
2. Crie conta (grátis)
3. Vá em "Developers" → "API Keys"
4. Copie sua key

### **Passo 2: Configurar** (1 minuto)

```bash
# Edite o arquivo .env
nano .env

# Adicione sua key:
BIRDEYE_API_KEY=sua_key_aqui
```

### **Passo 3: Executar** (30 segundos)

```bash
# Testar conexão
python test_connection.py

# Executar análise
PYTHONPATH=/home/user/moon-dev-ai-agents python src/agents/strategy_agent.py
```

**Tempo total: 3-4 minutos** ⏱️

---

## 🔄 OPÇÃO 3: MODO CONTÍNUO (Monitoramento 24/7)

**Deixar rodando e recebendo alertas:**

```bash
# Roda a cada 5 minutos, indefinidamente
./run_loop.sh
```

Você verá:
```
🟢 BUY Signal: RSI oversold + Volume surge
   Token: 9BB6NFE...
   Strength: 92%
   Position Size: $23

🤖 CONSENSUS: 4/5 strategies agree
✅ TRADE APPROVED
```

---

## 📊 O Que Acontece Quando Roda?

```
1. Busca dados de mercado (últimas 3 dias, 15min candles)
   ↓
2. Calcula indicadores (RSI, MACD, Bollinger, EMA)
   ↓
3. Gera sinais de 5 estratégias em paralelo
   ↓
4. Valida consenso (precisa 3+ concordando)
   ↓
5. Mostra oportunidade de trade no terminal
   ↓
6. (Opcional) Executa trade automaticamente
```

---

## 🎯 Configuração Mínima

**Arquivo:** `src/config.py`

```python
# Tokens para monitorar
MONITORED_TOKENS = [
    '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump',  # Adicione mais
]

# Estratégias
ENABLE_STRATEGIES = True
STRATEGY_MIN_CONFIDENCE = 0.7  # 70% mínimo

# Position sizing
usd_size = 10  # $10 por trade (comece pequeno)

# Timeframe
DATA_TIMEFRAME = '15m'  # 15 minutos
SLEEP_BETWEEN_RUNS_MINUTES = 5  # Verificar a cada 5min
```

---

## ⚠️ IMPORTANTE: Paper Trading vs Live Trading

### **PAPER TRADING (Padrão - Seguro)**
- ✅ Sistema analisa mercado
- ✅ Gera sinais
- ✅ Mostra oportunidades
- ❌ NÃO executa trades

### **LIVE TRADING (Requer configuração extra)**
Para executar trades reais, você precisa:

1. **Carteira Solana com fundos**
2. **Private key no .env**
3. **Descomentar código de execução** em `strategy_agent.py`

**⚠️ ATENÇÃO:** Live trading = dinheiro real. Sempre teste primeiro!

---

## 🎓 Entendendo os Sinais

Quando você roda, verá sinais assim:

```
📊 Estratégia 1: RSI + Volume Surge
   RSI: 28.5 (OVERSOLD 🔵)
   Volume: 2.1x (SURGE ⚡)

   🟢 BUY SIGNAL GENERATED!
   • Reason: RSI oversold with volume confirmation
   • Signal Strength: 92%
   • Recommended Position: $23
```

**Como interpretar:**
- **🟢 BUY** = Momento de compra identificado
- **🔴 SELL** = Momento de venda identificado
- **⚪ NO SIGNAL** = Esperando melhor setup
- **Strength 70-100%** = Nível de confiança

---

## 📁 Estrutura de Arquivos

```
📁 moon-dev-ai-agents/
├── 🚀 run_strategies_realistic.py    ← Execute isso primeiro!
├── 🔧 test_connection.py              ← Testa conexões
├── 🔄 run_loop.sh                     ← Loop contínuo
├── 📖 SETUP_REAL_TIME_TRADING.md     ← Guia completo
├── 📖 ESTRATEGIAS_RENTAVEIS.md       ← Detalhes das estratégias
├── ⚙️  setup_trading.sh               ← Setup automático
└── 📁 src/
    ├── strategies/custom/             ← Suas estratégias (privadas)
    ├── agents/strategy_agent.py       ← Agente principal
    └── config.py                      ← Configurações
```

---

## 🆘 Troubleshooting

### **Erro: "ModuleNotFoundError"**
```bash
pip install termcolor requests pandas numpy python-dotenv
```

### **Erro: "BIRDEYE_API_KEY não configurada"**
```bash
# Obtenha em: https://birdeye.so/
# Adicione ao .env:
BIRDEYE_API_KEY=sua_key_aqui
```

### **Nenhum sinal gerado**
- Normal! Estratégias esperam setups perfeitos
- Mercado pode estar neutro
- Tente outros tokens ou ajuste parâmetros

---

## 📞 Precisa de Ajuda?

1. **Guia Completo:** `cat SETUP_REAL_TIME_TRADING.md`
2. **Estratégias:** `cat ESTRATEGIAS_RENTAVEIS.md`
3. **Demo:** `python run_strategies_realistic.py`

---

## 🎯 Resumo: 3 Comandos Para Começar

```bash
# 1. Setup automático
./setup_trading.sh

# 2. Demo com dados simulados
python run_strategies_realistic.py

# 3. Modo real (após configurar API key)
python test_connection.py
```

---

**🌙 É isso! Você está pronto para encontrar oportunidades de trade! 🚀**

**Próximo passo:** Execute `python run_strategies_realistic.py` AGORA e veja funcionando!
