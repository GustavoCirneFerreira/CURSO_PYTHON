# def somar_listas():
#     lista1 = [1,2,3,4,5,6,7]
#     lista2 = [1,2,3,4]

#     lista_soma = []

#     for num1, num2 in zip(lista1, lista2):
#         lista_soma.append(num1 + num2)

#     return list(lista_soma)
    
# print(somar_listas())

# <------------------------------------------------->

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4]

lista_soma = []

for i in range(len(lista2)):
    lista_soma.append(lista1[i] + lista2[i])

print(lista_soma)
