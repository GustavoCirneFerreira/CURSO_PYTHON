import os

item_list = []

while True:
    inserir = input('\nSelecione uma opção: [I]nserir [A]pagar [L]istar : ').upper()

# INSERT ITEM IN SHOPPING LIST:
    if inserir == 'I':
        os.system('cls')
        item = input('\nInsira seu item no carrinho: ')
        item_list.append(item)

# CHECK SHOPPING LIST ITEMS:
    elif inserir == 'L':
        os.system('cls')
        i = 0
        for obj in item_list:
            print(i, obj)
            i += 1

# REMOVE ITEM FROM SHOPPING LIST: 
    elif inserir == 'A':
        os.system('cls') 
        try:
            remove = int(input('\nDiga qual índice você deseja remover: '))
            del item_list[remove]   
        except ValueError:
             print('\nPor favor digite números')
        except IndexError:
            print('\n Indíce fora de alcance.')
            


# WARINING FOR NOT FOLLOWING THE CODE:
    else:
        print('\nOpção não disponível.')
