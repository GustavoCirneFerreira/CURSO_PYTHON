import json

lista_fazer = []
lista_desfazer = []


def listar():
    print('TAREFAS')
    for item in lista_fazer:
        print(item)
    print()

def desfazer():
    try:
        item_desfeito = lista_fazer[-1]
        lista_desfazer.append(item_desfeito)
        lista_fazer.pop()

        print('TAREFAS')
        for item in lista_fazer:
            print(item)
        print()
    
    except IndexError:
        print('Nada a desfazer...')
        print()

def refazer():
    try:
        item_refeito = lista_desfazer[-1]
        lista_fazer.append(item_refeito)
        lista_desfazer.pop()

        print('TAREFAS')
        for item in lista_fazer:
            print(item)
        print()

    except IndexError:
        print('Nada a refazer...')
        print()

def salvar_dados():
    with open('dados_salvos.json', 'w+', encoding='utf-8') as arquivo:
        json.dump(lista_fazer, arquivo, indent=2)


while True:
    print('Comandos: listar, desfazer, refazer')
    print()
    entrada = input('Digite uma tarefa ou comando: ').lower()
    print()

    comandos = {
        'listar': lambda: listar(),
        'desfazer': lambda: desfazer(),
        'refazer': lambda: refazer(),
    }
    comando = comandos.get(entrada)


    if entrada == 'listar':
        listar()
        continue

    elif entrada == 'desfazer':
        desfazer()
        salvar_dados()
        continue

    elif entrada == 'refazer':
        refazer()
        salvar_dados()
        continue

    else:
        lista_fazer.append(entrada)

        print('TAREFAS')
        for item in lista_fazer:
            print(item)
        print()
        salvar_dados()
        continue