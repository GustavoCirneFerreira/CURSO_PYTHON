def vezes(inserir):
    def multiplicar(numero):
        return numero * inserir
    return multiplicar
    

multiplicar_por_dois = vezes(2)
multiplicar_por_tres = vezes(3)
multiplicar_por_cinco = vezes(5)

print(multiplicar_por_dois(10))
print(multiplicar_por_cinco(10))
print(multiplicar_por_tres(10))


