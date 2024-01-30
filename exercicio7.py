#MAKE A PROGRAM THAT PRINTS NATURAL NUMBERS FROM 0 TO 99,
#MAKE THEM HAVE AN ANSWER TO NUMBERS THAT ARE:
#DIVIDED BY 7,
#DIVIDED BY 11,
#DIVIDED BY 7 AND 2, AT THE SAME TIME

num_7 = []
num_11 = []
num_7_2 = []


for i in range(0, 100):
    if i % 7 == 0:
        num_7.append(i)
    if i % 11 == 0:
        num_11.append(i)
    if i % 7 == 0 and i % 2 == 0:
        num_7_2.append(i)

print('Divisiveis por 7: ', num_7)
print('Divisiveis por 11: ', num_11)
print('Divisiveis por 7 e 2: ', num_7_2)



