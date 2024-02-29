# RETURN THE SUM OF THE MULTIPLES OF 3 OR 5 BELOW THE NUMBER PASSED IN
# IF IT IS A MULTIPLE OF BOTH 3 AND 5, ONLY COUNT IT ONCE 

def multiplo_de_3_ou_5(numero_fim):
    lista_dos_multiplos = []

    for numeros in range(numero_fim):
        if numeros % 3 == 0 and numeros % 5 == 0:
            continue
            lista_dos_multiplos.append(numeros)
        if numeros % 3 == 0:
            lista_dos_multiplos.append(numeros)
        elif numeros % 5 == 0:
            lista_dos_multiplos.append(numeros)

        if numero_fim < 0:
            return 0

    return sum(lista_dos_multiplos)

print(multiplo_de_3_ou_5(30))



# for numeros in range(10):
#     print(numeros)
