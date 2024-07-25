import os

caminho_arquivo = r'C:\\Users\\Túlio Cirne\\Desktop\\CURSO_PYTHON\\'
caminho_arquivo += 'arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Lendo...')
#     arquivo.seek(0,0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
     ...
     print(type(arquivo))
     arquivo.write('Atenção\n')
     arquivo.write('Linha 2\n')
     arquivo.writelines(
         ('Linha 3\n', 'Linha 4\n')
     )

# os.remove(caminho_arquivo)
os.rename(caminho_arquivo, 'aula115.txt')