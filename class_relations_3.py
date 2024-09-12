# Composition

class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self._endereco = []

    def inseir_endereco(self, rua, numero):
        self._endereco.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self._endereco:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente = Cliente('Maria')

cliente.inseir_endereco('Av Brasil', 134)
cliente.inseir_endereco('Rua D', 780)
# print(cliente._endereco[0].rua)
# print(cliente._endereco[1].rua)

cliente.listar_endereco()

del cliente