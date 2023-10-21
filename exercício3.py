nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if (nome == '' or idade == ''):
    print('Você deixou campos vazios...')

elif (' ' in nome):
    print('\nSeu nome possui espaços')
    print(f'\nSeu nome é {nome}.')
    print('\nSeu nome invertido é', (nome[::-1]))
    print(f'\nSua idade é {idade}.')
    print(f'\nSeu nome tem', len(nome), 'letras')
    print('\nA primeira letra do seu nome é:', (nome[:1:]))
    print('\nA ultima letra do seu nome é:', (nome[-1::]))

else:
    print('\nSeu nome não possui espaços.')
    print('\nSeu nome invertido é', (nome[::-1]))
    print(f'\nSeu nome é {nome}.')
    print(f'\nSua idade é {idade}.')
    print('\nSeu nome tem', len(nome), 'letras')
    print('\nA primeira letra do seu nome é:', (nome[:1:]))
    print('\nA ultima letra do seu nome é:', (nome[-1::]))