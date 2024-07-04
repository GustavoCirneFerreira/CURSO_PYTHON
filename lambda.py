lista = [
    {'nome': 'Gustavo', 'sobrenome': 'Ferreira'},
    {'nome': 'Túlio', 'sobrenome': 'Ferreira'},
    {'nome': 'Ana', 'sobrenome': 'Rosa'},
    {'nome': 'Gabriel', 'sobrenome': 'Barbosa'}
]


def exibir(lista):
    for item in lista:
        print(item)
    print()

lista.sort(key= lambda item: item['nome'])
l2 = sorted(lista, key= lambda item:item['sobrenome'])

exibir(lista)
exibir(l2)

# <------------------------------------------------------->

# def executa(funcao, *args):
#     return funcao(*args)

# def soma(x,y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica



# print(executa(
#         lambda x, y: x + y, 
#         2, 3
# ), 
#     executa(soma, 2, 3)
#     )

# duplica = executa(
#     lambda m: lambda n: n * m,
#     2
# )

# print(duplica(2))

# print(executa(
#     lambda *args: sum(args),
#     1,2,3,4,5,6,7,8,8,9,10
# ))