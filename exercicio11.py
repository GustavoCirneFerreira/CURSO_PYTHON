#GIVEN TWO INT NUMBERS, 
#MULT THEM TOGETHER
#GET THE RESULT AND CHECK IF IT IS LESS THEN A 1000
#RETURN THEIR PRODUCT ONLY IF THE PRODUCT IS
#EQUAL OR LESS THEN 1000, OTHERWISE, RETURN THEIR SUM

# num1 = int(input('Diga o primeiro número: '))
# num2 = int(input('Diga o segundo número: '))

# res = num1 + num2

num1 = int(input('Diga o primeiro número: '))
num2 = int(input('Diga o segundo número: '))


def my_function(numb1, numb2):
    mult = numb1 * numb2
    sum = num1 + num2
    if mult <= 1000:
        print('Lower then 1000, printing product:', mult)
    else:
        print('Higher then 1000, printing sum:', sum)

my_function(num1, num2)
        
# def my_function(numb1, numb2):
#     prod = numb1 * numb2
#     if prod <= 1000:
#         return prod
#     else:
#         return numb1 + numb2

# num1 = int(input('Diga o primeiro número: '))
# num2 = int(input('Diga o segundo número: '))

# result = my_function(num1, num2)
# print('The result is:', result)



# def media(num1, num2):

# n = int(input('Enter number: '))
# sum = 0 

# for num in range(0, n + 1):
#     sum = sum + num
#     print(sum)
# print('Sum of first', n , 'numbers is: ', sum)
# average = sum / n
# print('Average of', n, 'is:', average)


    


