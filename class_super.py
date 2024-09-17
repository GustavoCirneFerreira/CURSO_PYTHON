# Super is the super class in sub classes
# Main class (Persona)
#   -> super class, base class, parent class
# Children class (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    def metodo(self):
        super(C, self).metodo()
        print('C')

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)