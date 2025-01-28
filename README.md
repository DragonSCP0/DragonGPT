# Chatbot AI com FastAPI

Este projeto implementa um chatbot utilizando FastAPI e OpenAI.

## Configuração do Ambiente no GitHub Codespaces

1. **Requisitos:**
   - Python 3.9 ou superior.
   - Ambiente configurado com 4 núcleos e 16 GB de RAM.

2. **Passos para Iniciar o Projeto:**
   - Clone este repositório no seu Codespaces.
   - Instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```
   - Inicie o servidor:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```

3. **Endpoint do Servidor:**
   O servidor estará acessível em:
   - `http://0.0.0.0:8000`
   - Ou pelo endpoint público do Codespace.

## Testando o Chatbot

- Teste com cURL:
  ```bash
  curl -X POST "http://0.0.0.0:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_input": "Explique o conceito de inteligência artificial."}'
