string = 'Gustavo'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
p1 = Pessoa('Gustavo', 'Cirne')

p2 = Pessoa('Roberto', 'Vargas')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)