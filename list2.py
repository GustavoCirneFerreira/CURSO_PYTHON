# APPEND - Adiciona um item ao final
# Insert - Adiciona um item no índice escolhido
# Pop - Remove um item no final ou no índice escolhido
# Del - Apaga um índice
# Clear - Limpa a lista
# Extend - Estende a lista
# + - Concatena listas

# lista = [1, 2, 3, 4, 5]
# lista.append('Luiz')
# lista.append(1223)
# del lista[-1]
# # lista.clear()
# lista.insert(500000, 5)
# print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)