# Liskov substitution principle:
#   Objetos da superclasse devem ser substituíveis 
#   por objetos de uma subclasse sem quebrar a aplicação

from abc import abstractmethod, ABC

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        print()

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: Enviando', self.msg)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: Enviando', self.msg)
        return True

def notificar(notificacao:Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')

notificar(NotificacaoEmail('Testando email'))
notificar(NotificacaoSMS('Testando SMS'))