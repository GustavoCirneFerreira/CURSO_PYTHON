# FOR:

# senha = ('12345')

# senha_digitada = input('Digite a sua senha: ')

# repetições = 0

# while senha_digitada != senha:
#     senha_digitada = input(f'Digite a sua senha novamente, essa é a tentativa {repetições}: ')

#     repetições += 1

#     if senha_digitada == senha:
#         break

texto = 'Python'

novo_texto = ''

for i in texto:
    novo_texto += f'*{i}'
    print(i)
print(novo_texto)