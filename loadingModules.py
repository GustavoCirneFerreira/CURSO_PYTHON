import importlib

import loadingModules_m

print(loadingModules_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(loadingModules_m) 

print('FIM')