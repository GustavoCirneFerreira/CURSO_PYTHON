# SECRET WORD CHALLENGE:
# MAKE A SECRET WORD WITH THE POSSIBILITY OF ONLY TYPING
# ONE LETTER

# WHEN THE USER TYPES YOU WILL CHECK IF THE LETTER IS IN
# THE SECRET WORD.
#   IF IT IS, SHOW THE LETTER; Word = python
#   IF THE LETTER ISNT, SHOW *.
# COUNT HOW MANY TIMES THE USER TRIED.

import os

palavra = 'gustavo'
letras_ac = ''
numero_tent = 0


print('<------------------------------------->')
print('       BEM VINDO AO JOGO DA PALAVRA                         ')
print('               SECRETA                                             ')
print('')
print('     A PALAVRA CONTÊM', len(palavra), 'letras...')
print('')
print('            BOA SORTE!                             ')
print('')


while True:
    chute = input('Qual será a letra que quer chutar? -> ')
    numero_tent += 1
    
    if len(chute) != 1:
        print('Apenas uma letra, por favor, digite uma letra.')
        continue

    if chute in palavra:
        letras_ac += chute
        

    for letra_secreta in palavra:
        if letra_secreta in letras_ac:
            print(letra_secreta)
        else:
            print('*')

    if len(letras_ac) == len(palavra):
        os.system('cls')
        print('Parábens! Você acertou todas as letras da palavra secreta!')
        print('Total de tentativas:', numero_tent)
        break
