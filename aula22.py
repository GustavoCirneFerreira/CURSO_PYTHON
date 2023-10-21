#Formatação básica de strings
#s = strings
#d = int
#f = float
#.<número de digitos> f
#x ou X = Hexadecimal
#(Caractere)(><^)(quantidade)
#> = Esquerda
#< = Direita
#^ = Centro
#Sinal = - ou +
#Conversion flags = !r !s !a

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:-^10}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{1000.000000000032433411324:+.1f}')
print(f'{variavel!r}')