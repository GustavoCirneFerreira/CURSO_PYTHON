import json

from exercicio29_a import CAMINHO_ARQUIVO, Pessoa, salvar_dados

# salvar_dados()

def ler_dados():
    with open (CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
        pessoas = json.load(arquivo)
        return pessoas
    

dados = ler_dados()

p1 = Pessoa(**dados[0])
p2 = Pessoa(**dados[1])
p3 = Pessoa(**dados[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

print(__name__)