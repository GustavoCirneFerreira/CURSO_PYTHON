# Try, except, else and finally
string = 'Luiz'# str
print(isinstance(string, str))

try:
    a = 18
    b = 0
    # print(b[0])
    print('LINHA 1')
    c = a / b
    print('LINHA 2')
    
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
except TypeError as error:
    print('TypeError')
    print('MSG', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUE')