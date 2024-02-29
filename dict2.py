# DICTIONARY METHODS

pessoa = {
    'nome': 'Gustavo',
    'sobrenome': 'Ferreira',
    'idade': 900,
}

pessoa.setdefault('idade', 90)
print(pessoa['idade'])

# print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

# for chave in pessoa.keys():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)

