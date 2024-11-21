# __new__ and __init__ in python classes

#   __new__ is the method responsible for 
# creating and returning an object. In this case,
# new receives cls
# __new__ MUST RETURN THE NEW OBJECT

#   __init__ is responsible for initiaing the instance,
# so it receives self.
# __init__ MUST RETURN NOTHING
# object is a super class of a class
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes da criação')
        criacao = super().__new__(cls)
        print('Depois da criação')
        criacao.x = 213
        return criacao

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'
    
a = A(123)
print(a.x)
