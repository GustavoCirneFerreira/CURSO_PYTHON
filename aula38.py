#Iterável => str, range, etc
#Iterador => que sabe entregar um valor por vez
#next => me entregue o próximo valor
#iter => me entregue SEU iterador

texto = 'Luiz' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        print('Acabou a string...')
        break

