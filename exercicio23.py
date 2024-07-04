# Crie uma função onde verifica se um número é duplicado,
# retorne como resposta o numero onde a sua segunda aparição
# veio primeiro do que os outros numeros

# def checar_numeros_duplicados():
#     lista_de_numeros = [1,4,9,8,9,4,8]
#     lista_checagem_numeros = []

#     for numero in lista_de_numeros:
#         if numero not in lista_checagem_numeros:
#             lista_checagem_numeros.append(numero)

#         elif numero in lista_checagem_numeros:
#             return numero
        
#         if lista_checagem_numeros == lista_de_numeros:
#             return -1
        
# print(checar_numeros_duplicados())

# <--------------------------------------------------------->

lista_de_listas_de_inteiros = [[1,2,6,7,1,3,5,1], [1,2,3,4,6,8,9,10]]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
            
        numeros_checados.add(numero)

    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_primeiro_duplicado(lista))

    