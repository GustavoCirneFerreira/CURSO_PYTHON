indice = 0
novo_nome = ''
nome = input('Qual é o seu nome? ')

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
