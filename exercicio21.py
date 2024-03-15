perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25'
    },  
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5'
    }
]

qtd_acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opção in enumerate(opcoes):
        print(f'{i}], {opção}')

    print()

    escolha = input('Escolha uma das opções de índices: ')

    escolha_int = None
    acertou = False
    qtd_opções = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opções:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True 

    if acertou:
        print('Acertou!')
        qtd_acertos += 1
    else:
        print('Errou...')

print(f'VOCÊ ACERTOU {qtd_acertos} vezes!')