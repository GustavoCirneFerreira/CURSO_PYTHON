#FOR:

# numeros = range(5, 10, 2)

# for numero in numeros:
#     print(numero)

num = int(input('Qual número que você quer para a tabuada? (APENAS NÚMEROS INTEIROS) '))

mult = num * 11

contador = 0

tabuada = range(0, mult, num)

for i in tabuada:
    print(f'{num}x{contador} = {i}')
    contador += 1