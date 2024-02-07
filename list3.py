# LOOK OUT FOR MUTABLE DATA
#   COPIED THE VALUE (NON MUTABLE)
#   POINTS TO THE SAME VALUE IN THE MEMORY (MUTABLE)

# a = 94
# b = 10
# og_value = b
# b = a
# print(a)
# print(b)
# print(og_value)

lista_a = ['José', 'Maria', 'Luiz']
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer Coisa'
print(lista_a)
print(lista_b)