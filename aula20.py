#Operadores in e not in:
#print(nome[0])
#print('t' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite qual letra deseja encontrar em seu nome: ')

if encontrar in nome:
    print(f'{encontrar} está dentro de {nome}')
else:
    print(f'{encontrar} não está dentro de {nome}')