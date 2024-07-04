# print(list(range(10)))
import pprint

lista = []
for numero in range(10):
    lista.append(numero)

# print(lista)

lista = [numero * 2
        for numero in range(10)]
# print(lista)

# Data maping in list comprehension:

produtos = [
    {'nome': 'p1', 'preco': 10, },
    {'nome': 'p2', 'preco': 20, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
print(*novos_produtos, sep='\n')

# lista = [n for n in range(10) if n < 5]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if produto['preco'] > 10
# ]
# print(novos_produtos)