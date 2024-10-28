# Class Methods + factories:
# It's methods where instead of "self", it's "cls".

# So instead of naming the first parameter,
# we receive the class.

class Pessoa:
    ano = 2023 # class atribute

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey!')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('Alberto', 20)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_com_50_anos('Roberto')

p4 = Pessoa.criar_sem_nome(30)
p5 = Pessoa.criar_sem_nome(28)
p6 = Pessoa.criar_sem_nome(10)


print(p4.nome, p4.idade)
print(p5.nome, p5.idade)
print(p6.nome, p6.idade)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)
# print()
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()