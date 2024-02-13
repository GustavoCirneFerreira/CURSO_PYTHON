# LISTS IN LISTS

salas = [
    # 0         1
    ['Maria',   'Helena'], # 0

    # 0             1
    ['Fernando',    'Jacinto'],  # 1

    # 0         1           #2
    ['Roberto', 'Gustavo', 'Gabriel',], # 2
]

# print(salas[0][1])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(f'Os alunos são: {aluno}')
        