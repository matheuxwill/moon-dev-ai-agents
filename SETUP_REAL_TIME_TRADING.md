# 🚀 GUIA COMPLETO: Setup para Trading em Tempo Real

## 📋 O Que Você Precisa Fazer (Checklist)

Este guia te mostra EXATAMENTE os passos para colocar os agentes rodando e recebendo oportunidades de trade reais.

---

## ✅ PASSO 1: Obter API Keys Necessárias

### **1.1 BirdEye API (OBRIGATÓRIO para dados de mercado)**

**O que é:** API para dados de tokens Solana (preço, volume, OHLCV)

**Como obter:**
1. Acesse: https://birdeye.so/
2. Crie uma conta
3. Vá em "Developers" → "API Keys"
4. Copie sua API key

**Custo:**
- Free tier: 100 requests/dia (suficiente para testes)
- Pro: $49/mês (unlimited requests)

---

### **1.2 Anthropic API (RECOMENDADO para validação LLM)**

**O que é:** Claude AI para validar sinais antes de executar trades

**Como obter:**
1. Acesse: https://console.anthropic.com/
2. Crie conta
3. "API Keys" → "Create Key"
4. Copie a key

**Custo:**
- Pay as you go: ~$0.01 por análise
- ~$3-5/mês para uso moderado

---

### **1.3 (OPCIONAL) Outras APIs**

```bash
# Para diversificar fontes de dados (opcional):
- CoinGecko API (grátis): https://www.coingecko.com/api
- Moon Dev API: https://moondev.com
```

---

## ✅ PASSO 2: Configurar Ambiente

### **2.1 Instalar Dependências**

```bash
# Navegue até o diretório do projeto
cd /home/user/moon-dev-ai-agents

# Ative o ambiente conda (se disponível)
conda activate tflow

# OU crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

**Nota:** Se `pandas-ta` falhar, instale assim:
```bash
pip install pandas ta-lib numpy
```

---

### **2.2 Configurar Arquivo .env**

Crie/edite o arquivo `.env` na raiz do projeto:

```bash
# Copie o template
cp .env_example .env

# Edite com suas keys
nano .env  # ou use seu editor preferido
```

**Conteúdo mínimo do .env:**
```bash
# === OBRIGATÓRIO ===
BIRDEYE_API_KEY=your_birdeye_key_here

# === RECOMENDADO ===
ANTHROPIC_KEY=your_anthropic_key_here

# === OPCIONAL ===
COINGECKO_API_KEY=your_coingecko_key_here
MOONDEV_API_KEY=your_moondev_key_here

# === TRADING (se quiser auto-execute) ===
SOLANA_PRIVATE_KEY=your_private_key_here  # CUIDADO! Nunca compartilhe
```

**⚠️ SEGURANÇA:**
- Nunca commite o arquivo `.env`
- Nunca compartilhe suas private keys
- Use carteira separada para testes

---

## ✅ PASSO 3: Configurar Tokens para Monitorar

### **3.1 Editar src/config.py**

```python
# Encontre essa seção:
MONITORED_TOKENS = [
    '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump',    # FART
    'DitHyRMQiSDhn5cnKMJV2CDDt6sVct96YrECiM49pump',    # Housecoin
    # Adicione mais tokens aqui
]
```

**Como encontrar endereços de tokens:**
1. Acesse https://birdeye.so/
2. Pesquise o token (ex: "BONK")
3. Copie o "Contract Address"
4. Adicione na lista acima

**Dicas:**
- Comece com 1-3 tokens para testar
- Escolha tokens com liquidez >$100k
- Verifique volume 24h >$50k

---

### **3.2 Configurar Parâmetros de Trading**

No mesmo arquivo `src/config.py`:

```python
# === ESTRATÉGIAS ===
ENABLE_STRATEGIES = True  # ✅ Certifique-se que está True
STRATEGY_MIN_CONFIDENCE = 0.7  # 70% mínimo (0.6 = mais agressivo, 0.8 = conservador)

# === POSITION SIZING ===
usd_size = 10  # Tamanho base da posição ($10 é seguro para começar)
max_usd_order_size = 5  # Tamanho máximo de uma ordem
MAX_POSITION_PERCENTAGE = 20  # Máximo 20% do capital por token

# === RISK MANAGEMENT ===
CASH_PERCENTAGE = 30  # Sempre manter 30% em USDC (buffer de segurança)
MAX_LOSS_USD = 20  # Parar se perder $20 em 12h
MAX_GAIN_USD = 100  # Realizar lucros em $100 em 12h
MINIMUM_BALANCE_USD = 50  # Balance mínimo antes de parar

# === TIMEFRAME ===
DATA_TIMEFRAME = '15m'  # 15 minutos (bom para day trading)
# Opções: '5m', '15m', '1H', '4H'

# === FREQUÊNCIA ===
SLEEP_BETWEEN_RUNS_MINUTES = 5  # Verificar mercado a cada 5 minutos
```

---

## ✅ PASSO 4: Testar Conexão com API

Antes de rodar o sistema completo, teste se tudo está funcionando:

```bash
# Teste 1: Verificar se API keys funcionam
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('BIRDEYE_API_KEY:', 'OK' if os.getenv('BIRDEYE_API_KEY') else 'MISSING')
print('ANTHROPIC_KEY:', 'OK' if os.getenv('ANTHROPIC_KEY') else 'MISSING')
"

# Teste 2: Testar conexão BirdEye
python -c "
import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump'
url = f'https://public-api.birdeye.so/defi/token_overview?address={token}'
headers = {'X-API-KEY': os.getenv('BIRDEYE_API_KEY')}
resp = requests.get(url, headers=headers)
print(f'BirdEye API: {resp.status_code}')
if resp.status_code == 200:
    print('✅ API funcionando!')
else:
    print('❌ Erro na API - verifique sua key')
"
```

---

## ✅ PASSO 5: Executar em Modo Teste (Paper Trading)

### **5.1 Primeira Execução - Apenas Monitoramento**

```bash
# Execute o strategy agent (SEM fazer trades)
PYTHONPATH=/home/user/moon-dev-ai-agents python src/agents/strategy_agent.py
```

**O que vai acontecer:**
- ✅ Buscar dados dos tokens configurados
- ✅ Calcular todos os indicadores (RSI, MACD, etc)
- ✅ Gerar sinais das 5 estratégias
- ✅ Validar consenso
- ✅ Mostrar decisão no terminal
- ❌ NÃO executa trades (modo read-only)

**Você verá algo assim:**
```
🔍 Analyzing 9BB6NFE... with RSI + Volume strategy
🟢 BUY Signal for 9BB6NFE...: RSI=28.5, Vol=2.1x, Strength=0.92

🤖 CLAUDE VALIDATION: APPROVED
✅ TRADE WOULD BE EXECUTED (paper trading)
   • Position Size: $23 (based on 92% strength)
```

---

### **5.2 Executar em Loop Contínuo**

Para monitorar continuamente:

```bash
# Crie um script de loop
cat > run_continuous.sh <<'EOF'
#!/bin/bash
while true; do
    echo "🔄 $(date): Running strategy analysis..."
    PYTHONPATH=/home/user/moon-dev-ai-agents python src/agents/strategy_agent.py
    echo "⏳ Waiting 5 minutes..."
    sleep 300  # 5 minutos
done
EOF

chmod +x run_continuous.sh
./run_continuous.sh
```

**Ou use o sistema nativo:**
```bash
# Execute o main.py que já tem loop interno
python src/main.py
```

---

## ✅ PASSO 6: Modo LIVE (Executar Trades Reais)

### **⚠️ ATENÇÃO: Leia com cuidado antes de ativar!**

### **6.1 Preparação Final**

**Checklist de Segurança:**
- [ ] Testou em paper trading por pelo menos 24h
- [ ] Entende os riscos (pode perder dinheiro)
- [ ] Configurou limites de perda (MAX_LOSS_USD)
- [ ] Tem saldo mínimo na carteira (>$100)
- [ ] Carteira tem SOL para gas fees (~$5)
- [ ] Nunca compartilhou sua private key

---

### **6.2 Configurar Carteira Solana**

```bash
# Gere ou importe sua private key
# OPÇÃO 1: Phantom/Solflare wallet
# Exporte a private key e adicione ao .env

# OPÇÃO 2: Gerar nova (para testes)
python -c "
from solders.keypair import Keypair
kp = Keypair()
print(f'Public Key: {kp.pubkey()}')
print(f'Private Key: {list(kp.secret())}')  # Adicione ao .env
"

# Adicione ao .env:
SOLANA_PRIVATE_KEY=your_private_key_array_here
```

**Envie fundos:**
1. Copie o Public Key
2. Envie SOL + USDC para essa carteira
3. Mantenha pelo menos:
   - $100 em USDC (para trades)
   - $5 em SOL (para gas fees)

---

### **6.3 Verificar nice_funcs.py**

O arquivo `src/nice_funcs.py` tem as funções de trade. Verifique:

```python
# Procure por essas funções:
def market_buy(token_address, amount_usd):
    # Executa compra

def market_sell(token_address, amount_usd):
    # Executa venda

def chunk_kill(token_address):
    # Fecha posição gradualmente
```

---

### **6.4 Ativar Auto-Trading**

No `src/agents/strategy_agent.py`, encontre:

```python
# Procure por essa linha (aproximadamente linha 200-300):
if approved_signals:
    for signal in approved_signals:
        # DESCOMENTE ESSAS LINHAS para executar trades reais:
        # if signal['direction'] == 'BUY':
        #     n.market_buy(signal['token'], usd_size * signal['signal'])
        # elif signal['direction'] == 'SELL':
        #     n.chunk_kill(signal['token'])
```

**Remova os comentários (#) para ativar:**
```python
if approved_signals:
    for signal in approved_signals:
        if signal['direction'] == 'BUY':
            n.market_buy(signal['token'], usd_size * signal['signal'])
        elif signal['direction'] == 'SELL':
            n.chunk_kill(signal['token'])
```

---

### **6.5 Executar com Auto-Trading Ativo**

```bash
# CUIDADO: Isso vai executar trades reais!
python src/main.py

# Ou apenas strategy agent:
PYTHONPATH=/home/user/moon-dev-ai-agents python src/agents/strategy_agent.py
```

---

## ✅ PASSO 7: Monitoramento e Logs

### **7.1 Onde Encontrar Logs**

```bash
# Logs dos agentes
ls src/data/strategy_agent/

# Ver últimos logs
tail -f src/data/strategy_agent/latest.log

# Ver trades executados
cat src/data/strategy_agent/trades.csv
```

---

### **7.2 Dashboard de Monitoramento (Opcional)**

Crie um script para ver status em tempo real:

```bash
cat > monitor.sh <<'EOF'
#!/bin/bash
while true; do
    clear
    echo "🌙 MOON DEV TRADING MONITOR"
    echo "======================================"
    echo ""
    echo "💰 WALLET BALANCE:"
    # Adicione comando para ver balance

    echo ""
    echo "📊 LAST SIGNALS:"
    tail -10 src/data/strategy_agent/signals.log

    echo ""
    echo "🔄 Refreshing in 30s..."
    sleep 30
done
EOF

chmod +x monitor.sh
./monitor.sh
```

---

## ✅ PASSO 8: Configurações Avançadas

### **8.1 Ajustar Estratégias**

Você pode desabilitar estratégias que não quer usar editando:

```python
# src/strategies/custom/__init__.py

# REMOVA estratégias que não quer:
__all__ = [
    'RSIVolumeStrategy',        # ← Mantenha
    'BollingerMeanReversionStrategy',  # ← Mantenha
    # 'MACDMomentumStrategy',   # ← Desabilitado
    'MultiIndicatorConfluenceStrategy',  # ← Mantenha
    # 'EMAVolumeStrategy'        # ← Desabilitado
]
```

---

### **8.2 Ajustar Parâmetros de Estratégias**

Edite os arquivos das estratégias para ajustar:

```python
# Exemplo: src/strategies/custom/private_rsi_volume_strategy.py

class RSIVolumeStrategy(BaseStrategy):
    def __init__(self):
        super().__init__("RSI + Volume Surge")

        # AJUSTE ESSES VALORES:
        self.rsi_period = 14           # Período do RSI
        self.rsi_oversold = 30         # Limite oversold (25 = mais agressivo)
        self.rsi_overbought = 70       # Limite overbought (75 = menos sinais)
        self.volume_surge_multiplier = 1.5  # Volume mínimo (2.0 = mais conservador)
```

---

## 📊 FLUXO COMPLETO EM TEMPO REAL

```
┌─────────────────────────────────────────────────┐
│ 1. LOOP INICIA (a cada 5 minutos)              │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 2. FETCH DATA via BirdEye API                  │
│    • Últimas 288 velas (3 dias, 15m)           │
│    • Para cada token em MONITORED_TOKENS       │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 3. CALCULAR INDICADORES                         │
│    • RSI, MACD, Bollinger, EMA, Volume          │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 4. GERAR SINAIS (5 estratégias em paralelo)    │
│    • Cada estratégia retorna: BUY/SELL/NEUTRAL │
│    • Com strength score (0-1)                   │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 5. VALIDAR CONSENSO                             │
│    • Precisa 3+ estratégias concordando         │
│    • Se sim → continua                          │
│    • Se não → rejeita e aguarda próximo loop    │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 6. VALIDAÇÃO LLM (Claude)                       │
│    • Analisa contexto de mercado                │
│    • Verifica razões dos sinais                 │
│    • Aprova ou rejeita                          │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 7. RISK MANAGEMENT CHECK                        │
│    • Balance suficiente?                        │
│    • Dentro dos limites de loss?                │
│    • Posição não excede max %?                  │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 8. EXECUTAR TRADE (se aprovado)                 │
│    • BUY: market_buy(token, $size * strength)   │
│    • SELL: chunk_kill(token)                    │
│    • Log resultado                              │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 9. SLEEP 5 MINUTOS                              │
│    → Volta para passo 1                         │
└─────────────────────────────────────────────────┘
```

---

## 🎯 CONFIGURAÇÃO RECOMENDADA PARA INICIANTES

```python
# src/config.py - Configuração CONSERVADORA

# === Tokens (comece com 1-2) ===
MONITORED_TOKENS = [
    '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump',  # FART
]

# === Estratégias ===
ENABLE_STRATEGIES = True
STRATEGY_MIN_CONFIDENCE = 0.75  # 75% mínimo (conservador)

# === Position Sizing (pequeno para começar) ===
usd_size = 5  # $5 por trade
max_usd_order_size = 5
MAX_POSITION_PERCENTAGE = 15  # Máximo 15% por token

# === Risk Management (proteções fortes) ===
CASH_PERCENTAGE = 40  # Manter 40% em cash
MAX_LOSS_USD = 10  # Parar se perder $10
MAX_GAIN_USD = 50  # Realizar em $50
MINIMUM_BALANCE_USD = 50  # Parar se balance < $50

# === Timeframe ===
DATA_TIMEFRAME = '1H'  # 1 hora (menos volátil)
SLEEP_BETWEEN_RUNS_MINUTES = 15  # Verificar a cada 15min
```

---

## ❓ FAQ - Perguntas Frequentes

### **Q: Quanto dinheiro preciso para começar?**
A: Mínimo $100 recomendado:
- $90 em USDC (para trades)
- $10 em SOL (gas fees)

### **Q: Quanto vou gastar em APIs?**
A:
- BirdEye: Free tier OK para começar (~100 requests/dia)
- Claude: ~$3-5/mês para uso moderado
- Total: ~$5-10/mês

### **Q: Os trades executam automaticamente?**
A: Só se você descomentar o código de execução no strategy_agent.py

### **Q: Posso rodar 24/7?**
A: Sim! Use um VPS ou deixe seu computador ligado.

### **Q: É rentável?**
A: NÃO HÁ GARANTIAS. Trading tem riscos. Pode perder dinheiro.

### **Q: Preciso entender de programação?**
A: Não para usar básico. Sim para customizar estratégias.

### **Q: Funciona em qualquer exchange?**
A: Atualmente: Solana DEX. HyperLiquid está em beta.

---

## ⚠️ AVISOS IMPORTANTES

1. **NUNCA compartilhe sua private key**
2. **SEMPRE teste em paper trading primeiro**
3. **USE limites de perda (stop loss)**
4. **Comece com valores PEQUENOS**
5. **Monitore diariamente** (pelo menos no início)
6. **Entenda que pode PERDER DINHEIRO**
7. **Não invista mais do que pode perder**

---

## 📞 Suporte

- **Documentação**: ESTRATEGIAS_RENTAVEIS.md
- **Issues**: https://github.com/anthropics/moon-dev-ai-agents/issues
- **Testes**: Use `python run_strategies_realistic.py` para simular

---

**🌙 Boa sorte nos seus trades! Comece pequeno, aprenda, e escale aos poucos. 🚀**
