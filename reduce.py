# Reduce - Makes a reduction of an iteable in a value
import functools

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Prod 5', 'preco': 10.00},
    {'nome': 'Prod 4', 'preco': 22.32},
    {'nome': 'Prod 3', 'preco': 10.11},
    {'nome': 'Prod 2', 'preco': 105.87},
    {'nome': 'Prod 1', 'preco': 69.90},
]

def funcao_do_reduce(acumulador, produto):
    print('acumulador',acumulador)
    print('produto',produto)
    return acumulador + produto['preco']



total = functools.reduce(
    funcao_do_reduce,
    produtos,
    0
)

total = functools.reduce(
    lambda a, p: a + p['preco'],
    produtos,
    0
)


# total = 0
# for prod in produtos:
#     total += prod['preco']

print(total)