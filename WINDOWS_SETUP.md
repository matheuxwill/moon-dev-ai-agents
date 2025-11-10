# 🪟 GUIA WINDOWS - Setup Rápido

## ❌ Erro Comum: "No such file or directory"

Você está no diretório errado! Os scripts estão dentro do repositório.

---

## ✅ SOLUÇÃO: Navegar até o Diretório Correto

### **Passo 1: Encontrar o Repositório**

O repositório foi clonado. Você precisa encontrá-lo. Tente estas localizações:

```powershell
# Opção 1: Procurar na pasta do usuário
cd ~
dir moon-dev-ai-agents

# Opção 2: Procurar em Documents
cd ~/Documents
dir moon-dev-ai-agents

# Opção 3: Procurar em Downloads
cd ~/Downloads
dir moon-dev-ai-agents

# Opção 4: Buscar em todo o sistema
Get-ChildItem -Path C:\ -Filter "moon-dev-ai-agents" -Directory -Recurse -ErrorAction SilentlyContinue
```

---

### **Passo 2: Navegar até o Repositório**

Quando encontrar, navegue até lá:

```powershell
# Exemplo (ajuste o caminho conforme encontrou):
cd C:\Users\willi\Documents\moon-dev-ai-agents

# OU
cd C:\Users\willi\Downloads\moon-dev-ai-agents

# OU onde quer que esteja
```

---

### **Passo 3: Verificar se Está no Lugar Certo**

```powershell
# Listar arquivos - deve ver os scripts
dir

# Deve mostrar algo como:
# run_strategies_realistic.py
# setup_trading.sh
# QUICK_START.md
# etc.
```

---

### **Passo 4: Executar o Script**

```powershell
python run_strategies_realistic.py
```

---

## 🚀 INSTALAÇÃO DO ZERO (Se não tiver o repo)

Se você não tem o repositório clonado ainda:

### **Opção A: Baixar ZIP**

1. Acesse: https://github.com/matheuxwill/moon-dev-ai-agents
2. Clique em "Code" → "Download ZIP"
3. Extraia para uma pasta (ex: `C:\trading\moon-dev-ai-agents`)
4. Navegue até a pasta:
   ```powershell
   cd C:\trading\moon-dev-ai-agents
   ```

### **Opção B: Clonar com Git**

```powershell
# Instale Git primeiro: https://git-scm.com/download/win

# Navegue para onde quer clonar
cd C:\Users\willi\Documents

# Clone o repositório
git clone https://github.com/matheuxwill/moon-dev-ai-agents.git

# Entre na pasta
cd moon-dev-ai-agents
```

---

## 📋 SETUP COMPLETO NO WINDOWS

### **1. Verificar Python**

```powershell
# Verificar se Python está instalado
python --version

# Deve mostrar: Python 3.x.x
# Se não tiver, baixe em: https://www.python.org/downloads/
```

### **2. Instalar Dependências**

```powershell
# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Se der erro de execução, rode isto primeiro:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Instalar dependências
pip install termcolor requests pandas numpy python-dotenv
```

### **3. Configurar .env (Opcional para dados reais)**

```powershell
# Copiar template
copy .env_example .env

# Editar com Notepad
notepad .env

# Adicionar sua BirdEye API key:
# BIRDEYE_API_KEY=sua_key_aqui
```

### **4. Executar Demo**

```powershell
python run_strategies_realistic.py
```

---

## ⚡ ATALHO RÁPIDO (Cole tudo de uma vez)

```powershell
# Navegar para Documents
cd ~/Documents

# Se o repo não existir, clonar
if (!(Test-Path moon-dev-ai-agents)) {
    git clone https://github.com/matheuxwill/moon-dev-ai-agents.git
}

# Entrar na pasta
cd moon-dev-ai-agents

# Criar ambiente virtual
python -m venv venv

# Ativar
.\venv\Scripts\Activate.ps1

# Instalar dependências mínimas
pip install termcolor requests pandas numpy python-dotenv

# Executar demo
python run_strategies_realistic.py
```

---

## 🐛 Troubleshooting Windows

### **Erro: "Activate.ps1 cannot be loaded"**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Erro: "git não é reconhecido"**

- Instale Git: https://git-scm.com/download/win
- Ou baixe o ZIP do GitHub

### **Erro: "python não é reconhecido"**

- Instale Python: https://www.python.org/downloads/
- ✅ Marque "Add Python to PATH" durante instalação

### **Erro: "ModuleNotFoundError"**

```powershell
pip install termcolor requests pandas numpy python-dotenv
```

---

## 📁 Estrutura de Pastas Esperada

Quando estiver no lugar certo, o `dir` deve mostrar:

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----                                            src
-a----                                            run_strategies_realistic.py
-a----                                            run_strategies_live.py
-a----                                            setup_trading.sh
-a----                                            test_connection.py
-a----                                            QUICK_START.md
-a----                                            SETUP_REAL_TIME_TRADING.md
-a----                                            README.md
```

---

## 🎯 Versão Simplificada (3 Passos)

```powershell
# 1. Baixar e extrair ZIP do GitHub
# https://github.com/matheuxwill/moon-dev-ai-agents

# 2. Navegar até a pasta extraída
cd C:\Users\willi\Downloads\moon-dev-ai-agents

# 3. Instalar dependências e executar
pip install termcolor requests pandas numpy python-dotenv
python run_strategies_realistic.py
```

---

## ✅ Como Saber se Deu Certo?

Você verá algo assim:

```
================================================================================
🌙 MOON DEV AI TRADING AGENTS - LIVE MARKET ANALYSIS 🚀
================================================================================

⚙️  System Configuration:
   • Exchange: Solana DEX
   • Monitored Tokens: 1
   • Timeframe: 15 minutes
   ...
```

---

## 💡 Dica Extra: Criar Atalho

Crie um arquivo `run.bat` no diretório:

```batch
@echo off
cd /d %~dp0
call venv\Scripts\activate.bat
python run_strategies_realistic.py
pause
```

Depois é só dar duplo clique em `run.bat`!

---

## 📞 Ainda Com Problemas?

1. Verifique onde está:
   ```powershell
   pwd  # Mostra diretório atual
   ```

2. Liste arquivos:
   ```powershell
   dir  # Deve ver run_strategies_realistic.py
   ```

3. Se não vir o arquivo, você está no lugar errado!

---

**🌙 Siga estes passos e vai funcionar! 🚀**
