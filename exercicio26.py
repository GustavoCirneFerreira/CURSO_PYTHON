import itertools

def zipper():
    lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    lista2 = ['BA', 'SP', 'MG', 'RJ']

    for cidade, estado in zip(lista1, lista2):
        print(f'{cidade} {estado}')

zipper()


def zipper_alternativo():
    lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    lista2 = ['BA', 'SP', 'MG', 'RJ']
    
    return list(itertools.zip_longest(lista1, lista2, fillvalue= 'SEM CIDADE'))

print(zipper_alternativo())