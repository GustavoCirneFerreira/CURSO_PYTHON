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
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('Minha nota')

        return True


with MyContextManager('context_manager.txt', 'w') as arquivo:
    print('WITH', arquivo)
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')