class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._fabricante = None
        self._motor = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
v6 = Motor('V6')

fusca.motor = v6
fusca.fabricante = volkswagen

uno = Carro('Uno')
fiat = Fabricante('Fiat')

uno.motor = v6
uno.fabricante = fiat

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
print(uno.nome, uno.fabricante.nome, uno.motor.nome)