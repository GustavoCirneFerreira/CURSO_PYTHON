import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Eduardo', '45')
p2 = Pessoa('Renata', '30')
p3 = Pessoa('Rennan', '13')

# print(p1.__dict__)

bd = [p1.__dict__, p2.__dict__, p3.__dict__]

CAMINHO_ARQUIVO = 'exercicio_29.json'

def salvar_dados(info):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(info, arquivo, indent=2, ensure_ascii=True)
    return info


# if __name__ == '__main__':
#     print('ELE É O MAIN')
#     salvar_dados(bd)