# Decorar = Add / Remove / Restrict / Change

# def criar_funcao(func):
#     def interna(*args, **kwargs):

#         print('Vou te decorar:')

#         for arg in args:

#             is_string(arg)

#         resultado = func(*args, **kwargs)

#         resultado += 'QUALQUER'

#         print(f'O seu resultado foi {resultado}.')

#         print('Ok, agora você foi decorado.')

#         return resultado
    
#     return interna

# @criar_funcao
# def inverte_string(string):
#     return string[::-1]


# def is_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string.')


# invertida = inverte_string('OK')
# print(invertida)

# <----------------------------------------------------------->

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decorator 1')

        def aninhada(*args, **kwargs):
            print('Parametros do decorador:', 1,2,3)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,2,3)
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)