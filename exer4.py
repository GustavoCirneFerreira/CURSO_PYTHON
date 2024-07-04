quant_brinq = int(input('Quantos brinquedos há no parque? '))
altura_carlinhos = int(input('Qual é a altura de Carlinhos(em centimetros)? '))
cont = 1
lista_altura_brinquedos = []

for brinq in range(quant_brinq):
    altura_brinq = int(input(f'Qual é a altura mínima do brinquedo {cont}? ' ))
    cont += 1
    lista_altura_brinquedos.append(altura_brinq)

    if altura_brinq <= 90 or altura_brinq >= 200:
        print('Tamanho minimo/máximo atingido. Por favor, repita a altura.')
        break 

for altura in lista_altura_brinquedos:
    if altura_carlinhos < altura:
        quant_brinq -= 1
        
print(f'A quantidade de brinquedos que Carlinhos é permitido entrar são: {quant_brinq}')
        
if quant_brinq >= 6 or altura_brinq < 1:
    print('Quantidade de brinquedos minimo/máximo atingido. Por favor, repita a quantidade')