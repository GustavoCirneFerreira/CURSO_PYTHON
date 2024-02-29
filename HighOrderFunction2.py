# CLOSURE:

def criarSaudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criarSaudacao('Bom Dia')
falar_bom_noite = criarSaudacao('Boa Noite')

for nome in ['Gustavo', 'Túlio', 'Madu']:
    print(falar_bom_dia(nome))
    print(falar_bom_noite(nome))