#Fatiamento de strings:
#012345687
#Olá mundo
#-987654321
#Fatiamento [i:f:p] [::]
#Obs.: a função len retorna a QUANTIDADE de 
#caracteres da string.

variavel = 'Olá'
# print((variavel[:1:]))
# print((variavel[-1::]))
# print(variavel[::1])
# print (variavel[::-1])

if len(variavel) > 4:
    print('Funcionou!')
else:
    print('Funcionou também!')