word = 'JavaScript'.lower()
word_Java = input('Digite a palavra que está dentro').lower()

def wordCheck(word_choice):
    if word_choice in word:
        print(f'The word {word_choice} is in {word}')

wordCheck(word_Java)
