class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade

# dados = {'idade': 30, 'outra': 'coisa'}
# p1 = Pessoa(**dados)
# p1 = Pessoa(idade=30, outra='coisa')

p1 = Pessoa('João', 30)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# print(p1.__dict__)
# del p1.__dict__['nome']
# print(vars(p1))
# print(p1.nome)
print(vars(p1))
print(p1.nome)

# p1 = Pessoa('João', 35)
# p2 = Pessoa('Helena', 12)
# print(Pessoa.ano_atual)

# Pessoa.ano_atual = 1

# print(p1.get_ano_de_nascimento())
# print(p2.get_ano_de_nascimento())
