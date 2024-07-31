def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_cliente('Luiz')
adiciona_cliente('Joana', cliente1)
adiciona_cliente('Fernando', cliente1)
print(cliente1)

cliente2 = adiciona_cliente('Renata')
adiciona_cliente('Fogaça', cliente2)
print(cliente2)
