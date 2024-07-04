# UNPACKAGING IN METHODS AND FUNCTIONS:

string = 'ABCD'
lista = ['Maria', 'Eduarda', 1, 2, 3, 'Helena']
tupla = 'python', 'é', 'legal'

salas = [
    # 0         1
    ['Maria',   'Helena'], # 0

    # 0             1
    ['Fernando',    'Jacinto'],  # 1

    # 0         1           #2
    ['Roberto', 'Gustavo', 'Gabriel',], # 2
]


a, b, *_, u= lista
print(a, u)

print(*lista)
print(*salas, sep='\n')