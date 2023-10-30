# Resto de divisão:

# numero = input('Digite um número inteiro: ')
# numero_par_ou_impar = (float(numero) % 2)

# if numero_par_ou_impar == 0:
#     print('O número é par.')
# else:
#     print('O número é impar.')

# if numero.isdigit():
#     ...
# else:
#     print('Não é um número inteiro...')

# or e and (else e elif):

# hora = input('Que horas são agora? ')

# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom Dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa Tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa Noite!')
#     else:
#         print('Não conheço essa hora...')

# except:
#     print('Por favor, apenas números inteiros...')

# Fatiamento de string:

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto!')

elif tamanho_nome <= 5 and tamanho_nome <=6:
    print('Seu nome é normal!')

elif tamanho_nome >= 7:
    print('Seu nome é muito grande!')