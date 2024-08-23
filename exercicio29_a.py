import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Eduardo', '45')

# print(p1.__dict__)

CAMINHO_ARQUIVO = 'exercicio_dados.json'

def salvar_dados(info):
    dados = info
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        dados = json.dump(info, arquivo, indent=2, ensure_ascii=True)
    return dados

salvar_dados(p1.__dict__)

