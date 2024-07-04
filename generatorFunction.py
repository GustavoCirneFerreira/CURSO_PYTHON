# def generator(n=0, maximum=10):
#     while True:
#         yield n

#         n += 1

#         if n > maximum:
#             return

    # yield 1  #Paused
    # print('Continuando...')
    # yield 2 # Paused
    # print('Mais um...')
    # yield 3 
    # print('Fim do yield.')
    # return 'ACABOU!'

# gen = generator(maximum=10000)

# for n in gen:
#     print(n)
# <-------------------------------------------->

# Yield from:

def gen1():
    yield 1
    yield 2
    yield 3
    yield 4

def gen2(gen):
    yield from gen()
    yield 5
    yield 6

g = gen2(gen1)

for n in g:
    print(n)
