# DICTIONARY METHODS

import copy

# pessoa = {
#     'nome': 'Gustavo',
#     'sobrenome': 'Ferreira',
#     'idade': 900,
# }

# pessoa.setdefault('idade', 90)
# print(pessoa['idade'])

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave in pessoa.keys():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# d1 = {
#     'c1': 3,
#     'c2': 5,
#     'l1': [0,1,2]
# }

# d2 = copy.deepcopy(d1)

# d2['l1'][1] = 1000000
# d2['c1'] = 1000
# print(d1)
# print(d2)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update(nome= 'novovalor', idade= 30)
# tupla = ('nome', 'novo valor'), ('idade', 30)
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)

