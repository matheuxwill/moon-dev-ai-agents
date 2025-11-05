# 🚀 Estratégias de Trading Rentáveis - Moon Dev AI Agents

## 📊 Visão Geral

Este documento descreve **5 estratégias avançadas de trading** implementadas no sistema Moon Dev AI Agents. Cada estratégia foi projetada com base em princípios comprovados de análise técnica e otimizada para maximizar rentabilidade.

---

## 🎯 Estratégias Implementadas

### 1. **RSI + Volume Surge Strategy** 🔥
**Arquivo:** `src/strategies/custom/private_rsi_volume_strategy.py`

**Tipo:** Mean Reversion (Reversão à Média)

**Como Funciona:**
- Detecta condições de **oversold** (RSI < 30) e **overbought** (RSI > 70)
- Requer confirmação de **volume 1.5x acima da média** para validar o sinal
- Quanto mais extremo o RSI, maior a força do sinal (até 100%)

**Parâmetros:**
```python
RSI Period: 14
RSI Oversold: 30 (Extreme: 20)
RSI Overbought: 70 (Extreme: 80)
Volume Multiplier: 1.5x
```

**Quando Usar:**
- ✅ Mercados laterais/choppy
- ✅ Tokens com alta volatilidade
- ✅ Após movimentos exagerados de preço

**Rentabilidade Esperada:** Alta em mercados ranging, moderada em tendências fortes

---

### 2. **Bollinger Bands Mean Reversion Strategy** 📈
**Arquivo:** `src/strategies/custom/private_bollinger_strategy.py`

**Tipo:** Mean Reversion (Reversão à Média)

**Como Funciona:**
- Compra quando o preço toca a **banda inferior** + RSI oversold
- Vende quando o preço toca a **banda superior** + RSI overbought
- Calcula distância do preço às bandas para ajustar confiança

**Parâmetros:**
```python
BB Period: 20
BB Standard Deviation: 2.0
RSI Oversold: 35
RSI Overbought: 65
```

**Quando Usar:**
- ✅ Mercados laterais com ranges definidos
- ✅ Tokens consolidados após grandes movimentos
- ✅ Períodos de baixa volatilidade

**Rentabilidade Esperada:** Muito alta em ranging markets, baixa em strong trends

---

### 3. **MACD Momentum Breakout Strategy** 🚀
**Arquivo:** `src/strategies/custom/private_macd_momentum_strategy.py`

**Tipo:** Trend Following (Seguidor de Tendência)

**Como Funciona:**
- Detecta **cruzamentos MACD** (linha cruza sinal)
- Valida com **histograma crescente** para confirmar momentum
- Requer **volume 1.3x acima da média** para filtrar falsos sinais

**Parâmetros:**
```python
MACD Fast: 12
MACD Slow: 26
MACD Signal: 9
Volume Multiplier: 1.3x
```

**Quando Usar:**
- ✅ Mercados em tendência forte
- ✅ Breakouts confirmados
- ✅ Tokens com momentum claro

**Rentabilidade Esperada:** Alta em trending markets, baixa em choppy markets

---

### 4. **Multi-Indicator Confluence Strategy** 🎯
**Arquivo:** `src/strategies/custom/private_confluence_strategy.py`

**Tipo:** High Confidence Signals (Sinais de Alta Confiança)

**Como Funciona:**
- Combina **5 indicadores**: RSI, MACD, EMA (9/21), Volume, Price Momentum
- Só gera sinal quando **4 ou mais indicadores concordam**
- Calcula score de confluência (4/5 = 0.8, 5/5 = 1.0)

**Indicadores Analisados:**
```python
RSI: < 40 (buy) / > 60 (sell)
MACD: Crossover + Histogram
EMA: Fast (9) vs Slow (21) alignment
Volume: 1.4x above average
Price Momentum: Direction confirmation
```

**Quando Usar:**
- ✅ Quando você quer **máxima certeza**
- ✅ Entradas conservadoras
- ✅ Reduzir falsos positivos

**Rentabilidade Esperada:** Moderada/Alta com menor frequência de trades (alta precisão)

---

### 5. **EMA Crossover + Volume Confirmation** ⚡
**Arquivo:** `src/strategies/custom/private_ema_volume_strategy.py`

**Tipo:** Trend Following (Seguidor de Tendência)

**Como Funciona:**
- Sistema **Triple EMA** (9/21/50) para confirmar tendências
- Sinal de compra: EMA 9 cruza acima EMA 21, ambas acima EMA 50
- Sinal de venda: EMA 9 cruza abaixo EMA 21, ambas abaixo EMA 50
- Volume deve ser **1.5x acima da média**

**Parâmetros:**
```python
EMA Fast: 9
EMA Medium: 21
EMA Slow: 50
Volume Multiplier: 1.5x
Min EMA Separation: 0.3%
```

**Quando Usar:**
- ✅ Início de novas tendências
- ✅ Breakouts de consolidação
- ✅ Tokens com momentum sustentado

**Rentabilidade Esperada:** Alta em trending markets, baixa em choppy markets

---

## 🛠️ Como Usar as Estratégias

### Passo 1: Ativar o Sistema de Estratégias

Edite `src/config.py`:

```python
# Trading Strategy Agent Settings
ENABLE_STRATEGIES = True  # ✅ Certifique-se de que está True
STRATEGY_MIN_CONFIDENCE = 0.7  # Confiança mínima para executar trades (0-1)
```

### Passo 2: Configurar Tokens para Monitorar

No `src/config.py`, adicione os tokens que deseja analisar:

```python
MONITORED_TOKENS = [
    '9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump',  # Exemplo: FART
    'DitHyRMQiSDhn5cnKMJV2CDDt6sVct96YrECiM49pump',  # Exemplo: Housecoin
    # Adicione mais tokens aqui
]
```

### Passo 3: Executar o Sistema

**Opção A: Rodar o Orchestrator Completo**
```bash
conda activate tflow
python src/main.py
```
Isso executa todos os agentes ativos, incluindo o StrategyAgent.

**Opção B: Rodar Apenas o Strategy Agent**
```bash
conda activate tflow
python src/agents/strategy_agent.py
```
Executa apenas o agente de estratégias.

### Passo 4: Monitorar Sinais

As estratégias geram sinais coloridos no terminal:

```
🟢 BUY Signal for 9BB6NFE...: RSI=28.5, Vol=2.1x, Strength=0.92
   Aligned: RSI oversold, MACD bullish, Volume surge
```

```
🔴 SELL Signal for 9BB6NFE...: Price at upper BB, RSI=72.3, Strength=0.85
```

---

## 📊 Matriz de Seleção de Estratégia

| Condição de Mercado | Estratégia Recomendada | Rentabilidade Esperada |
|---------------------|------------------------|------------------------|
| **Ranging/Lateral** | RSI + Volume, Bollinger Bands | ⭐⭐⭐⭐⭐ |
| **Tendência Forte** | MACD Momentum, EMA Crossover | ⭐⭐⭐⭐⭐ |
| **Incerto/Misto** | Multi-Indicator Confluence | ⭐⭐⭐⭐ |
| **Alta Volatilidade** | RSI + Volume | ⭐⭐⭐⭐ |
| **Baixa Volatilidade** | Bollinger Bands | ⭐⭐⭐ |
| **Breakout** | MACD Momentum, EMA Crossover | ⭐⭐⭐⭐⭐ |

---

## 💡 Dicas para Maximizar Rentabilidade

### 1. **Combine Múltiplas Estratégias**
As estratégias funcionam em paralelo. Se várias estratégias concordarem, a confiança é maior.

### 2. **Ajuste Parâmetros para Seu Perfil**
```python
# Mais agressivo (mais sinais, menos confiança)
STRATEGY_MIN_CONFIDENCE = 0.6

# Mais conservador (menos sinais, mais confiança)
STRATEGY_MIN_CONFIDENCE = 0.8
```

### 3. **Use Validação LLM**
O sistema passa todos os sinais por Claude para validação adicional antes de executar.

### 4. **Gestão de Risco**
Configure limites no `config.py`:
```python
usd_size = 25  # Tamanho base da posição
MAX_POSITION_PERCENTAGE = 30  # Máximo 30% do capital em uma posição
CASH_PERCENTAGE = 20  # Sempre manter 20% em USDC
MAX_LOSS_USD = 25  # Parar se perder $25
```

### 5. **Timeframe Adequado**
```python
DATA_TIMEFRAME = '15m'  # Para day trading
DATA_TIMEFRAME = '1H'   # Para swing trading
DATA_TIMEFRAME = '4H'   # Para position trading
```

---

## 🎓 Entendendo os Sinais

### Estrutura do Sinal
```python
{
    'token': '9BB6NFE...',
    'signal': 0.85,          # Força do sinal (0-1)
    'direction': 'BUY',      # BUY, SELL, ou NEUTRAL
    'metadata': {
        'strategy_type': 'rsi_volume_surge',
        'rsi': 28.5,
        'volume_ratio': 2.1,
        'signal_strength': 0.85,
        'reasoning': 'RSI oversold (28.5) with 2.1x volume surge'
    }
}
```

### Interpretação da Força do Sinal
- **0.9 - 1.0**: 🟢 Sinal extremamente forte - Alta confiança
- **0.8 - 0.9**: 🟢 Sinal forte - Boa confiança
- **0.7 - 0.8**: 🟡 Sinal moderado - Confiança média
- **< 0.7**: 🔴 Abaixo do threshold - Não executado (se MIN_CONFIDENCE = 0.7)

---

## 🔬 Backtesting das Estratégias

Para testar as estratégias antes de usar capital real, use o RBI Agent:

```bash
python src/agents/rbi_agent.py
```

Ou crie um backtest customizado:

```python
from backtesting import Backtest, Strategy
from src.strategies.custom.private_rsi_volume_strategy import RSIVolumeStrategy
import pandas as pd

# Carregue dados OHLCV
data = pd.read_csv('src/data/rbi/BTC-USD-15m.csv')

# Configure e execute backtest
bt = Backtest(data, RSIVolumeStrategy, cash=10000, commission=0.002)
stats = bt.run()
print(stats)
bt.plot()
```

---

## 📞 Suporte

- **GitHub Issues**: https://github.com/anthropics/moon-dev-ai-agents/issues
- **Discord**: [Moon Dev Community]
- **YouTube**: [Moon Dev Channel]

---

## ⚠️ Disclaimer

**RISCO DE PERDA**: Trading de criptomoedas envolve risco substancial de perda. Estas estratégias são **experimentais e educacionais**. Não há garantia de rentabilidade.

- Sempre teste em paper trading primeiro
- Nunca invista mais do que pode perder
- Use gestão de risco apropriada
- Este projeto é open source e gratuito

---

## 🌙 Desenvolvido por Moon Dev

Built with 🚀 by the Moon Dev community

**Contribua**: Este é um projeto open source! Pull requests são bem-vindos.

**Próximas Estratégias Planejadas:**
- Ichimoku Cloud Strategy
- Fibonacci Retracement Strategy
- Order Flow Imbalance Strategy
- Whale Wallet Following Strategy
- Social Sentiment Strategy (Twitter/Discord)

---

**Última Atualização:** 2025-11-05
**Versão:** 1.0.0
