# Filter - filter is a functional filter

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Prod 5', 'preco': 10.00},
    {'nome': 'Prod 4', 'preco': 22.32},
    {'nome': 'Prod 3', 'preco': 10.11},
    {'nome': 'Prod 2', 'preco': 105.87},
    {'nome': 'Prod 1', 'preco': 69.00},
]

# novos_produtos = [
#     p for p in produtos 
#     if p['preco'] > 10]

novos_produtos = filter(
    lambda p: p['preco'] > 100,
    produtos
)
    

print_iter(produtos)
print_iter(novos_produtos)