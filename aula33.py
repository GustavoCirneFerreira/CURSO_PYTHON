# Repetições:
# while
# Executa uma ação enquanto uma condição estiver verdadeira:
# Loop Infinito = Quando o código não tem fim...

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:  
    coluna = 1
    while coluna <= qtd_colunas:  
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou...')