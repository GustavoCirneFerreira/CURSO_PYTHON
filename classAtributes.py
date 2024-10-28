class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade

# p1 = Pessoa('João', 35)
# p2 = Pessoa('Helena', 12)
print(Pessoa.ano_atual)

# Pessoa.ano_atual = 1

# print(p1.get_ano_de_nascimento())
# print(p2.get_ano_de_nascimento())
