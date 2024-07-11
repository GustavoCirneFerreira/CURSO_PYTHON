# Map - to map 
import functools
import types

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Prod 5', 'preco': 10.00},
    {'nome': 'Prod 4', 'preco': 22.32},
    {'nome': 'Prod 3', 'preco': 10.11},
    {'nome': 'Prod 2', 'preco': 105.87},
    {'nome': 'Prod 1', 'preco': 69.00},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = functools.partial(
    aumentar_porcentagem, porcentagem=1.1
)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} 
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

gen = (x for x in produtos)

novos_produtos = map(
    muda_preco_de_produtos, 
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorExit))
print(isinstance(gen, GeneratorExit))

print(list(map(
    lambda x: x * 3,
    [1,2,3,4]
    )))