# 🚀 GUIA SIMPLES - Rode em 3 Passos

## PASSO 1: Baixar o Projeto

### Opção A: Download ZIP (Mais Fácil)
1. Acesse: https://github.com/matheuxwill/moon-dev-ai-agents
2. Clique no botão verde **"Code"**
3. Clique em **"Download ZIP"**
4. Extraia o ZIP em qualquer pasta (ex: `C:\trading\`)

### Opção B: Git Clone
```bash
git clone https://github.com/matheuxwill/moon-dev-ai-agents.git
cd moon-dev-ai-agents
```

---

## PASSO 2: Instalar Dependências

```bash
# Windows PowerShell
cd C:\trading\moon-dev-ai-agents
pip install -r requirements.txt

# Linux/Mac
cd ~/moon-dev-ai-agents
pip install -r requirements.txt
```

**Se der erro**, instale apenas o essencial:
```bash
pip install termcolor requests pandas numpy python-dotenv
```

---

## PASSO 3: Rodar

### Demo Simples (SEM API keys):
```bash
python run_strategies_realistic.py
```

### Com Dados Reais (PRECISA de API key):
```bash
# 1. Obtenha API key em: https://birdeye.so/ (grátis)

# 2. Crie arquivo .env
# Windows:
notepad .env

# Linux/Mac:
nano .env

# 3. Adicione dentro do arquivo:
BIRDEYE_API_KEY=sua_key_aqui

# 4. Execute:
python src/agents/strategy_agent.py
```

---

## 🎯 É ISSO!

**Demo rápido:**
```bash
python run_strategies_realistic.py
```

**Com dados reais:**
```bash
# Configurar .env primeiro
python src/agents/strategy_agent.py
```

**Loop contínuo:**
```bash
# Linux/Mac
./run_loop.sh

# Windows
# Crie run.bat com:
# @echo off
# :loop
# python run_strategies_realistic.py
# timeout /t 300
# goto loop
```

---

## ⚠️ Problemas Comuns

**"python não reconhecido"**
- Instale: https://www.python.org/downloads/

**"ModuleNotFoundError"**
```bash
pip install termcolor requests pandas numpy python-dotenv
```

**"No such file"**
- Você não está na pasta do projeto
- Use `cd` para navegar até a pasta extraída/clonada

---

## 📁 Estrutura do Projeto

```
moon-dev-ai-agents/
├── run_strategies_realistic.py  ← Execute este!
├── src/
│   ├── agents/
│   │   └── strategy_agent.py    ← Ou este (com API key)
│   ├── strategies/custom/       ← Suas estratégias (privadas)
│   └── config.py                ← Configurações
├── .env                         ← API keys aqui
└── requirements.txt             ← Dependências
```

---

## 🎮 Comandos Principais

```bash
# Demo
python run_strategies_realistic.py

# Real (precisa API key)
python src/agents/strategy_agent.py

# Todos os agentes
python src/main.py
```

Pronto! É só isso mesmo.
