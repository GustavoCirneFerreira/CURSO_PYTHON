import json

string = 'Gustavo'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
p1 = Pessoa('Gustavo', 'Cirne')

p2 = Pessoa('Roberto', 'Vargas')

CAMINHO_ARQUIVO = 'exercicio29_a'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)

dados = []

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    dados = json.dump(p1.nome, arquivo, indent=2, ensure_ascii=True)
    dados = json.dump(p1.sobrenome, arquivo, indent=2, ensure_ascii=True)

    
