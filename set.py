# set(iterable) or {1,2,3}
# - they dont have indexes;
# - they dont guarantee order;
# - they are iterable: (for, in, not in);
# - their values are always unique;

# s1 = set('Gustavo')
# l1 = [1,2,3,3,3,3,3,1]
# s1 = set(l1)
# l2 = list(s1)
# s1 = {1,2,3}
# for numero in s1:
#     print(numero)

# <-------------------------->
# METHODS:

s1 = set()
s1.add('Luiz')
s1.add(1)
# s1.update(('Olá Mundo!',1,2,3,4))
# # s1.clear()
# s1.discard('Olá Mundo!')
print(s1)

# <-------------------------------------->
# USEFUL OPERATORS:

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # union
s3 = s1 & s2 # intersection (itens presentes em ambos os sets)
s3 = s2 - s1 # diference (itens apenas presentes no set da esquerda)
s3 = s2 ^ s1 # symmetrical diference (itens que não estão em ambos)
print(s3)