import json

# pessoa = {
#     'nome': 'Gustavo',
#     'sobrenome': 'Cirne',
#     'enderecos':
#     [
#         {'rua': 'R1', 'numero': '134'},
#         {'rua': 'R2', 'numero': '210'}
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2,4,6,8,10),
#     'dev': True,
#     'nada': None
# }

with open('aula_nova.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa['nome'])