import json

def carregar_treinamentos():
    with open("GPT/treinamento.json", "r") as file:
        treinamentos = json.load(file)
    return treinamentos["treinamentos"]

def salvar_novo_treinamento(novo_treinamento):
    treinamentos = carregar_treinamentos()
    treinamentos.append(novo_treinamento)
    
    with open("GPT/treinamento.json", "w") as file:
        json.dump(treinamentos, file, indent=4)
    
    print("Novo treinamento salvo com sucesso.")
