# INTRODUCTION TO UNPACKING + TUPLES
# TUPLES ARE IMUTABLE LISTS
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
nomes = list(nomes)
nomes[0] = 'Dédé'
print(nomes)
print(nomes[0])