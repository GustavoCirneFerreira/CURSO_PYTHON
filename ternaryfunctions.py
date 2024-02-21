# <VALUE> if <CONDITION> else <ANOTHER VALUE>
import random

# condicao = 10 == 11
# variavel = 'valor' if condicao else 'deu errado'
# print(variavel)

digito = random.randint(0, 11)
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if False else 'Outro Valor' if False else 'Fim')