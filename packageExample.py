# import sys

# import package.modulo_package
# from package.modulo_package import soma_do_modulo
# from package import modulo_package

# print(__name__)

# print(soma_do_modulo(1,2)) 
# print(package.modulo_package.soma_do_modulo(2,1))
# print(modulo_package.soma_do_modulo(2,1))

# print(*sys.path, sep='\n')

# <------------------------------------------------------->
# from package.modulo_package import soma_do_modulo, fala_oi
# fala_oi()

import package

from package import soma_do_modulo, variavel, fala_oi
print(soma_do_modulo(2,3))