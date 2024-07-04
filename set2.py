letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('PARABENS, ENCONTROU A LETRA MISTERIOSA')
        break
    
    print(letras)

# lista = [1,2,3,4,5,6,6,6,1]
# set1 = set(lista)
# print(set1)
