# SPLIT AND JOIN WITH LISTS AND STRINGS:

frase = '           Olha.só.que            ,            coisa.interesssante.               '
lista_palavras_cruas = frase.split(',')

lista_palavras = []

for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())

# print(lista_palavras)
# print(lista_palavras_cruas)
frases_unidas = ' '.join(lista_palavras)
print(frases_unidas)

lista_sem_pontos = frases_unidas.split('.')

print(lista_sem_pontos)

frase_unida_de_vdd = ''.join(lista_sem_pontos)

print(frase_unida_de_vdd)




# plvr = 'Ronaldo'
# lista_ronaldo = list('')

# for letra in plvr:
#     plvr.split()
#     lista_ronaldo.append(letra)
    
# reverse = lista_ronaldo[::-1]

# print(reverse)






