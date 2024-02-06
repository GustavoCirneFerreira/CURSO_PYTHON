# LISTS 
# SUPPORTS ANY TYPE OF VALUES
# INDEXES AND
# GOOD METHODS TO KNOW: APPEND, INSERT, POP, DEL, CLEAR,
# EXTEND, +
# CREATE, READ, UPDATE, DELETE = lista[i]
#         012345;
#        -12345;
string = 'ABCDE'

# lista = [123, 'comida', 2.5, True]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2])) 

# i = 0

# lista = ['Fernando', 'Gustavo', 'Arthur']

# for pessoa in lista:
#     i += 1
#     print(pessoa, i)

lista = [1, 2, 3, 4]
# lista[2] = 300
# print(lista[2])
# print(lista)
# del lista[2]
# print(lista[2])
# print(lista)
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print('Item removido da lista:', ultimo_valor)