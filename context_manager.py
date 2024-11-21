# Context Manager

#   To create a context manager, the __enter__ and __exit__
# methods must be implemented.

#   The __exit__ method will receive an exception class,
# the exception and the traceback. If it returns True,
# exception in with will be deleted.
#  Ex:
# with open ('context_manager.txt', 'w') as arquivo:
class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquvivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquvivo, self.modo, encoding='utf8')

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

with MyContextManager('context_manager.txt', 'w') as arquivo:
    print('WITH', arquivo)