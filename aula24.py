# Try/Except
# Try = Tentar executar o código
# Except = Ocorreu algum erro ao tentar executar

# print(1234)
# print(567)
# int('a')
numero_str = input('Vou dobrar o número que vou digitar que você: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f} ')
    
except:
    print('Isso não é um número.')
    
# if numero_str.isdigit():
#     print(numero_str.isdigit())
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f} ')
# else:
#     print('Apenas números sem ponto.')