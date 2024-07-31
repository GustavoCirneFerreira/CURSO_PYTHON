# Try, except, else and finally
# string = 'Luiz'# str
# print(isinstance(string, str))
lista = []
try:

    rivo = lista[-1]
    # print(b[0])
    print('LINHA 1')
    print('LINHA 2')
    
except IndexError as e:
    print('Bão pode')
except NameError:
    print('Nome b não está definido')
except TypeError as error:
    print('TypeError')
    print('MSG', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUE')