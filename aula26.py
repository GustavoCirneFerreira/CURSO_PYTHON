# Flag = Marcar um local
# None = Não valor
# is e is not = É ou não é (tipo, valor, identidade)
# id = Identificação

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = False 
passou_no_if = None # Checagem de Flag para ver se o if 
                    # foi alterado. Dependendo da resposta,
                    # saberemos a sua rota 
                    # e por onde está passando.

if condicao:
    passou_no_if = True # Flag dentro do if, alterando
                        # o valor do passou_no_if.
    print('Faça alguma coisa...')
else:
    print('Faça outra coisa...')


# Checagem de alteração no passou_no_if,
# dependendo da resposta, saberemos por onde passou:
if passou_no_if is None:
    print('Não passou no if.')
else:
    print('Passou no if.')



