import json

def carregar_respostas():
    with open("GPT/respostas.json", "r") as file:
        respostas = json.load(file)
    return respostas["respostas"]

def analisar_pergunta(pergunta_usuario):
    respostas = carregar_respostas()
    
    # Procurar resposta existente
    resposta = next((r["resposta"] for r in respostas if r["pergunta"] == pergunta_usuario), None)
    
    return resposta
