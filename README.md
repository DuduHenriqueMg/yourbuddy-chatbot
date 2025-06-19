# YourBuddy - Chatbot de Assistência Psicológica

YourBuddy é um chatbot desenvolvido em Python com Streamlit que utiliza a API da OpenAI para fornecer suporte psicológico e orientações de bem-estar mental.

- **Link:** [https://yourbuddy.streamlit.app/](https://yourbuddy.streamlit.app/)

## ⚠️ Aviso Importante

Este chatbot é apenas uma ferramenta de apoio e **não substitui** o acompanhamento profissional de um psicólogo ou psiquiatra. Em casos de emergência ou crises graves, procure ajuda profissional imediatamente.

## 🚀 Funcionalidades

- Interface conversacional amigável 
- Respostas empáticas baseadas em assitente de IA
- Design acessível

## 📋 Pré-requisitos

- Python 3.13+
- Chave de API da OpenAI
- Git (opcional)

## 🛠️ Instalação

### Opção 1: Usando pip

```bash
# Clone o repositório
git clone https://github.com/DuduHenriqueMg/yourbuddy-chatbot/
cd yourbuddy-chatbot

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# ou
.venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt
```
### Opção 2: Usando uv (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/DuduHenriqueMg/yourbuddy-chatbot/
cd yourbuddy-chatbot

# Instale o uv se não tiver
pip install uv

# Crie e ative o ambiente virtual
uv venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Instale as dependências
uv pip install -r requirements.txt
```

## ⚙️ Configuração da Chave da API

### Método 1: Arquivo .env

1. Crie um arquivo `.env` na raiz do projeto:
```bash
touch .env
```

2. Adicione sua chave da OpenAI:
```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

### Método 2: Streamlit Secrets

1. A pasta `.streamlit` já existe no projeto

2. Crie o arquivo `secrets.toml` dentro da pasta `.streamlit`:
```bash
touch .streamlit/secrets.toml
```

3. Adicione sua chave no arquivo `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "sk-sua-chave-aqui"
```

## 🏃‍♂️ Executando a Aplicação

```bash
streamlit run app.py
```

Ou se estiver usando uv:
```bash
uv run streamlit run psibot.py
```

## 📁 Estrutura do Projeto

```
yourbuddy-chatbot/
├── psibot.py              
├── requirements.txt       
├── .env                  # Variáveis de ambiente (não versionar)
├── .streamlit/
│   └── secrets.toml      # Secrets do Streamlit (não versionar)
├── .gitignore
├── pyproject.toml
├── .python-version
└── README.md
```

## 🔒 Segurança

- **Nunca** commite arquivos `.env` ou `secrets.toml`
- Monitore o uso da API para evitar custos excessivos

## 📦 Dependências

```txt
streamlit>=1.28.0
openai>=1.0.0
python-dotenv>=1.0.0
```

## 🚀 Deploy Streamlit 

### Streamlit Cloud (Temporário)
1. Faça push do código para GitHub
2. Conecte no [Streamlit Cloud](https://streamlit.io/cloud)
3. Configure os secrets na interface web

### Outras Plataformas
- Configure as variáveis de ambiente conforme a documentação da plataforma
- Use `requirements.txt` para instalação das dependências

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

