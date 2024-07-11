# groupby - grouping values
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A',},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D',},
    {'nome': 'João', 'nota': 'A',},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key= ordena)
grupos = groupby(alunos_agrupados, key= ordena)

# for aluno in alunos_agrupados:
#     print(aluno)

 

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))