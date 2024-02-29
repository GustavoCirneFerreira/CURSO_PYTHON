# MAKE A FUNCTION THAT RECEIVES A LIST WITH NUMBERS AND
# STRINGS INSIDE OF IT, WITH THE OBJECTIVE OF FILTERING
# AND PRINTING OUT ONLY THE INTEGERS OF THE LIST

def filtroDeNumeros(lista):
    lista_filtrada_numeros = []
    for i in lista:
        if type(i) == int:
            lista_filtrada_numeros.append(i)
    print(lista_filtrada_numeros)

filtroDeNumeros(['1', 5, '3', 'roberto', 7, 1, 4])
filtroDeNumeros([1,'a','b',0,15])