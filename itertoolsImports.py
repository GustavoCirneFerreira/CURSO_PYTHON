from itertools import combinations, permutations, product

# Combination - order doesn't matter - iterable + group size


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = ['João', 'Joana', 'Luiz', 'Letícia']

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))