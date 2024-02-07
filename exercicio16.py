item_list = []

try:
    while True:
        inserir = input('Selecione uma opção: [I]nserir [A]pagar [L]istar : ').upper()

# INSERT ITEM IN SHOPPING LIST:
        if inserir == 'I':
            item = input('\nInsira seu item no carrinho: ')
            item_list.append(item)

# CHECK SHOPPING LIST ITEMS:
        if inserir == 'L':
            i = 0
            for obj in item_list:
                print(i, obj)
                i += 1

# REMOVE ITEM FROM SHOPPING LIST: 
        if inserir == 'A':
            remove = int(input('\nDiga qual índice você deseja remover: '))
            del item_list[remove]

# WARINING FOR NOT FOLLOWING THE CODE:
        if inserir != 'I' and inserir != 'A' and inserir != 'L':
            print('\nOpção não disponível.')
            continue

except:
    print('\nNão pode remover produtos em indices não existentes...')