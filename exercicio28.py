import json


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

def adicionar():
    lista_fazer.append(entrada)

    print('TAREFAS')
    for item in lista_fazer:
        print(item)
    print()

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe...')
        salvar_dados(tarefas, caminho_arquivo)
    return dados

def salvar_dados(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=True)
    return dados

CAMINHO_ARQUIVO = 'aula_119.json'

lista_fazer = ler([], CAMINHO_ARQUIVO)
lista_desfazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    print()
    entrada = input('Digite uma tarefa ou comando: ').lower()
    print()

    comandos = {
        'listar': lambda: listar(),
        'desfazer': lambda: desfazer(),
        'refazer': lambda: refazer(),
        'adicionar': lambda: adicionar()
    }
    comando = comandos.get(entrada) if comandos.get(entrada) is not None else \
        comandos['adicionar']
    comando()
    salvar_dados(lista_fazer, CAMINHO_ARQUIVO)



    # if entrada == 'listar':
    #     listar()
    #     continue

    # elif entrada == 'desfazer':
    #     desfazer()
    #     continue

    # elif entrada == 'refazer':
    #     refazer()
    #     continue
