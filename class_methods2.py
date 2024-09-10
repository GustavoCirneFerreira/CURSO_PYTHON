# method - self, instance method
# @classmethod - cls
# @staticmethod - No cls and no self

class Connection:
    
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    

    def set_user(self, user):
        #setter
        self.user = user

    def set_password(self, password):
        #setter
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


c1 = Connection()
c1.set_user('Gustavo')
print(c1.user)
c1.set_password('Guga1234')
print(c1.password)

c2 = Connection.create_with_auth('Roberta', 'obncOUBN28ONId')
print(c2.host, c2.user, c2.password)