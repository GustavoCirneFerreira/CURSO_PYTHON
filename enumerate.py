lista = ['Joao', 'Patrick', 'Roberto']

lista_enumerada = list(enumerate(lista))
lista.append('João')

# print(lista_enumerada)

for index, nome in enumerate(lista):
    print(index, nome)

# SAME THING AS THIS:

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)   

# WHICH IS THE SAME AS THIS:

# for tupla_enumerada in enumerate(lista):
#     print('FOR DA TUPLA:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
    
