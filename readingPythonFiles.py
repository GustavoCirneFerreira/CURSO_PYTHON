caminho_arquivo = 'C:\\Users\\Túlio Cirne\\Desktop\\pasta_teste\\'
caminho_arquivo += 'arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá Mundo!')
    print('Arquivo fechado!')