# Repetições:
# while
# Executa uma ação enquanto uma 
# condição estiver verdadeira:

condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')