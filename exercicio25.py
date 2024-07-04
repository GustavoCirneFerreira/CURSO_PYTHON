# Exercicio - Interrupting functions:

def soma(x, y):
    return x + y

def multilpica(x, y):
    return x * y 

def criar_funcao(funcao, x):
    def valor_y(y):
        return funcao(x, y)
    return valor_y


soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(10))

multiplica_com_dez = criar_funcao(multilpica, 10)
print(multiplica_com_dez(5))