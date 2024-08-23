import json

CAMINHO_ARQUIVO = 'exercicio_dados.json'

def ler_dados():
    dados = {}
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    return dados

dados = ler_dados()

print(dados)