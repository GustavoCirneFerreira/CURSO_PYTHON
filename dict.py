# pessoa = {
#     'nome': 'Gustavo',
#     'Sobrenome': 'Ferreira'
# }

# pessoa = dict(nome= 'Gustavo', sobrenome='GWRE')
# print(pessoa, type(pessoa))

# print(pessoa['nome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])



pessoa = {}
chave = 'nome_completo'

pessoa[chave] = 'Gustavo'
pessoa['sobrenome'] = 'Ferreira'
# del pessoa['sobrenome']

print(pessoa)

pessoa[chave] = 'Felipe'

print(pessoa[chave])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NAO EXISTE')   
else:
    print(pessoa['sobrenome'])

