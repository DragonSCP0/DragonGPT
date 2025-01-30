from GPT.carregar_dados import carregar_treinamentos, carregar_respostas, salvar_novo_treinamento
from web_validacao.validacao_web import coletar_dados_da_web, salvar_dados_web
from GPT.analise_perguntas import analisar_pergunta

def iniciar_ia():
    pergunta_usuario = input("Qual é a sua pergunta? ")
    
    resposta = analisar_pergunta(pergunta_usuario)
    
    if not resposta:
        print("Não encontrei a resposta nos dados, pesquisando na web...")
        dados_web = coletar_dados_da_web(pergunta_usuario)
        
        resposta_web = None
        for dado in dados_web:
            if dado["validade"] == "verdadeira":
                resposta_web = dado["texto"]
                break
        
        if resposta_web:
            print(f"Resposta encontrada na web: {resposta_web}")
            novo_treinamento = {
                "data": "2025-01-01",
                "informacoes": [{"pergunta": pergunta_usuario, "resposta": resposta_web, "fonte": dado["url"], "validade": "verdadeira"}]
            }
            salvar_dados_web(novo_treinamento)
        else:
            print("Nenhuma resposta válida encontrada na web.")
    
    else:
        print(f"Resposta: {resposta}")
    
    novo_treinamento = {
        "data": "2025-01-01",
        "informacoes": [{"pergunta": pergunta_usuario, "resposta": resposta}]
    }
    salvar_novo_treinamento(novo_treinamento)

if name == "main":
    iniciar_ia()
