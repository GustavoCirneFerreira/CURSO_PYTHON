# try:
#     import sys
#     sys.path.append('C:/Users/Túlio Cirne/Desktop/CURSO_PYTHON')
# except ModuleNotFoundError:
#     ...
# import modulo_python

# import test_m


# print('ESSE MODULO SE CHAMA', __name__)
# print(*sys.path, sep='\n')

# <--------------------------------------------------->

# YOU CAN IMPORT SPECIFIC VARIABLES FROM ANOTHER MODULE:
import test_m
from test_m import variavel_modulo, soma


# print('Este módulo se chama:', __name__)
print(test_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(test_m.soma(2, 3))


