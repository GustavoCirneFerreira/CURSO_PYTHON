menu = {
    '1': ['cachorro quente', 1.20],
    '2': ['coxinha', 3.20],
    '3': ['abacate', 2.20],
}

codigo = input('Informe o código: ')

if codigo in menu:
    valor_item = menu.get(codigo)
    quant = int(input('Quanto desse item você quer?'))
    valor_total = valor_item[1] * quant
    print(valor_total)
