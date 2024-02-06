# CHECK IF 3 NUMBERS ARE THE SAME,
# IF YES, RETURN 30
# OTHERWISE RETURN 20
# IF TWO NUMBERS ARE THE SAME, RETURN 40

num1 = int(input('Diga o primeiro número: '))
num2 = int(input('Diga o segundo número: '))
num3 = int(input('Diga o terceiro número: '))



def calc(numb1, numb2, numb3):
    if numb1 == numb2 and numb2 == numb3:
        print('All numbers are identical, printing result: 30')
    elif numb1 == numb2 or numb2 == numb3 or numb3 == numb1:
        print('All numbers are different, printing result: 40')
    else:
        print('All numbers are different, printing result: 20')
        
    

calc(num1, num2, num3)