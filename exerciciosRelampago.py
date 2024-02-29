# EXERCICIOS COM REVISÃO DE FUNÇÕES:

def mult(*args):
    result = 1
    for numero in args:
        result *= numero
    return result

def parOuImpar(numb):
    if numb % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

print(mult(1,3,5,7,3,1,4,2))

print(parOuImpar(16))

