# Associtation:

class Escritor():
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta():
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo...'
    
escritor = Escritor('Renato')

lapis = Ferramenta('Lápis de desenho')

maquina_de_escrever = Ferramenta('Máquina de escrever')

escritor.ferramenta = maquina_de_escrever

print(lapis.escrever())
print(maquina_de_escrever.escrever())

print(escritor.ferramenta.escrever())