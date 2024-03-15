def disponibilidade(mtbf):
    def tempo_entre_falhas(mttr):
        return (mtbf / (mttr + mtbf) * 100)
    return tempo_entre_falhas


def confiabilidade_sem_falhas(mtbf):
    return 2.71 ** (-8760 / mtbf) * 100

# print(format(confiabilidade_sem_falhas(24000), '.3f'))

print(format(disponibilidade(8760)(12),'.3f'))
print(format(disponibilidade(8760)(48),'.3f'))
print(format(disponibilidade(147)(21),'.2f'))


#    15 18 21 24 3 6 9
# print(3*7) # mttr

#  24 3 6 9 12 15 18 21 / 

# print(3*6)

