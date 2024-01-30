list = [1, 'Roberto', 2, 'Gustavo', 3, 'Burro']

nums = []
nomes = []

for i in list:
    if type(i) == int:
        nums.append(i)
    if type(i) == str:
        nomes.append(i)

# print('Nomes: ', nomes)
# print('Numeros:', nums)
