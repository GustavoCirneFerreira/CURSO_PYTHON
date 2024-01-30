#WRITE AN ARRAY CONTAINING ALL EVEN NUMBERS FROM 30 TO 70,
#WRITE AN ARRAY CONTAINING ALL ODD NUMBERS 
#FROM 10 TO 103 (103 NOT INCLUDED)
#WRITE AN ARRAY CONTAINING DECIMAL NUMBERS THAT ENDED WITH
#X.5 FROM 0 TO 10 (10 INCLUDED)

num_even_70 = []
num_odd_103 = []
num_dec_10 = []

#BETTER WAY TO FIX SOME ISSUES:
#num = range(30, 71)
#for num_par in num:

for num_par in range(30, 72):
    if num_par % 2 == 0:
        num_even_70.append(num_par)

for num_impar in range(10, 103):
    if num_impar % 2 != 0:
        num_odd_103.append(num_impar)

#DOESN'T WORK BECAUSE THERE IS NO np.arange(start, stop, step)
# for num_dec in range (0, 11, 0.5):
#     if num_dec % 2 != 0:
#         num_dec_10.append(num_dec)


print('Números pares de 30 a 70:', num_even_70)
print('\nNúmeros ímpares de 10 a 103:', num_odd_103, '\n')
# print('Números decimais de 0 a 10:', num_dec_10)



 