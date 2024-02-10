# def duplicate_encode(word):
#     for letter in word:
#         if word.count(letter) > 1:
#             ...

def stringCount():
    word = 'Onomatopeia'.lower()
    for letter in word:
        if word.count(letter) > 1:
            word = word.replace(letter, ')')
        else:
            word = word.replace(letter, '(')
    print(word)

stringCount()