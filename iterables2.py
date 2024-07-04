import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__


generator = (n for n in range(10000))
print(sys.getsizeof(generator))
