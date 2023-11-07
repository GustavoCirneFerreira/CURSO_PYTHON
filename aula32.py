# Repetições:
# while
# Executa uma ação enquanto uma condição estiver verdadeira:
# Loop Infinito = Quando o código não tem fim...

contador = 0

while contador <= 100:
    contador += 1
    

    if contador == 6:
        print('O 6 SUMIU!')
        continue
        
    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}')
        continue
    
    print(contador)

    if contador == 40:
        break
    
    
print('Acabou')