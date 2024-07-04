lista = []
for x in range(3):
    for y in range(3):
        if y > 1:
            continue
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3) 
]

lista = [
    [letra for letra in 'Gustavo']
    for x in range(3)
]
print(lista)   