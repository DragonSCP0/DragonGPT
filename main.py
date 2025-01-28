from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Configure sua chave da API OpenAI
openai.api_key = "SUA_API_KEY_AQUI"

# Inicializa o FastAPI
app = FastAPI()

# Modelo para receber solicitações
class UserRequest(BaseModel):
    user_input: str

# Rota de exemplo para verificar o status do servidor
@app.get("/")
def read_root():
    return {"status": "AI is running", "message": "Send your request to /chat"}

# Endpoint principal do chatbot
@app.post("/chat")
async def chat_with_ai(request: UserRequest):
    try:
        # Solicitação ao GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Substitua pelo modelo que você configurou
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.user_input},
            ],
            max_tokens=4096  # Limite alto de tokens para lidar com entradas grandes
        )
        return {"response": response.choices[0].message["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

