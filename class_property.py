class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # @property
    # def cor_tinta(self):
    #     print('PROPERTY')
    #     return self.cor

    def get_cor(self):
        print('GET COR!')
        return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())

