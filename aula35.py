#ITERANDO STRINGS

frase = 'Python é uma linguagem de programação'\
'multiparadigma'\
'Python foi criado por Guido Van Rossum'.lower()

i = 0
quant_vezes_letra_mais = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    quant_vezes_letra = frase.count(letra_atual)
    
    if quant_vezes_letra_mais < quant_vezes_letra:
        quant_vezes_letra_mais = quant_vezes_letra 
        letra_mais_vezes = letra_atual 

    i += 1 
    
print(f'A letra que apareceu mais vezes foi a letra {letra_mais_vezes}'
      f' com {quant_vezes_letra_mais} vezes que apareceu.')