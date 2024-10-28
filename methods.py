# Methods in Python class instances
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')



string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()