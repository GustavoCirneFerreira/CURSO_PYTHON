# Keeping states inside of the class:

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando...')
            return
        
        print(f'{self.nome} está fotografando')
        self.foto = True

    def parar_de_filmar(self):
        if self.filmando:
            print(f'{self.nome} parou de filmar...')
            self.filmando = False
            return
        
        print(f'{self.nome} JÁ está desligada...')

        
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.fotografar()
c1.parar_de_filmar()

