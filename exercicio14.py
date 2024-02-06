num1 = int(input('Diga um número: '))
num2 = int(input('Diga outro número:'))

list_of_numbers = range(50, 99)


def numbcheck(numb1, numb2):
    if numb1 and numb2 in list_of_numbers:
        print('Os dois números estão entre 50 a 99')
    else:
        print('Um ou os dois números não estão dentro da lista de números....')

numbcheck(num1, num2)