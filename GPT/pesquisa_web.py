import requests
from bs4 import BeautifulSoup

def validar_fonte(url):
    fontes_confiaveis = ["https://www.wikipedia.org", "https://www.bbc.com", "https://www.nytimes.com"]
    return any(fonte in url for fonte in fontes_confiaveis)

def coletar_dados_da_web(query):
    url = f"https://www.google.com/search?q={query}"
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.text, "html.parser")
    
    resultados = sopa.find_all('h3')
    dados = []
    
    for resultado in resultados:
        link = resultado.find_parent('a')['href']
        if validar_fonte(link):
            dados.append({"texto": resultado.get_text(), "url": link})
    
    return dados
