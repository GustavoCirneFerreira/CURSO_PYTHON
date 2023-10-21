#Interpolação básica de Strings:
#%s = string
#d e i = inteiro
#f = float
#x e X = Hexadecimal (ABCDEF0123456789)

nome = 'Gustavo Cirne'
preco = 10.00
variavel = '%s, o preço total foi de R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' %(15,15))