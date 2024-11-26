from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'está chamando', self.phone)
        return 123

call = CallMe(2134515356)
retorno = call('Gustavo')
print(retorno)