# 1 - cachorro quente = 4.00
# 2 - x salada = 4.50
# 3 - x bacon = 5.00
# 4 - torrada simples = 2.00
# 5 - refrigerante = 1.50

cq = 4.00
xs = 4.50
xb = 5.00
ts = 2.00
re = 1.50

codigo = int(input())
if codigo == 1:
    quant = int(input())
    resposta = cq * quant
    print(f'Total: R$ {resposta:.2f}')

if codigo == 2:
    quant = int(input())
    resposta = xs * quant
    print(f'Total: R$ {resposta:.2f}')


if codigo == 3:
    quant = int(input())
    resposta = xb * quant
    print(f'Total: R$ {resposta:.2f}')


if codigo == 4:
    quant = int(input())
    resposta = ts * quant
    print(f'Total: R$ {resposta:.2f}')

if codigo == 5:
    quant = int(input())
    resposta = re * quant
    print(f'Total: R$ {resposta:.2f}')