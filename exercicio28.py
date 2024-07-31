lista_fazer = []
lista_desfazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    print()
    entrada = input('Digite uma tarefa ou comando: ').lower()
    print()

    if entrada == 'listar':
        print('TAREFAS')
        for item in lista_fazer:
            print(item)
        print()
        continue

    elif entrada == 'desfazer':
        try:
            item_desfeito = lista_fazer[-1]
            lista_desfazer.append(item_desfeito)
            lista_fazer.pop()

            print('TAREFAS')
            for item in lista_fazer:
                print(item)
            print()
            continue

        except IndexError:
            print('Nada a desfazer...')
            print()
            continue

    elif entrada == 'refazer':
        try:
            item_refeito = lista_desfazer[-1]
            lista_fazer.append(item_refeito)
            lista_desfazer.pop()

            print('TAREFAS')
            for item in lista_fazer:
                print(item)
            print()
            continue

        except IndexError:
            print()
            print('Nada a refazer...')
            print()
            continue

    else:
        lista_fazer.append(entrada)

        print('TAREFAS')
        for item in lista_fazer:
            print(item)
        print()
        continue
