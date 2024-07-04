# def numeros_para_horas(numero):
#     segundos = 0
#     minutos = 0
#     horas = 0
#     for segundos in range(numero):
#         if segundo >= 60:
#             minutos += 1
#         if minutos >= 60:
#             horas += 1

# segundos = int(input('Diga o número para conversão: '))

# for sec in range(segundos):
#     if sec <= 60:
      
#       minuto += 1
#     # if sec <= 60:
    #     print(sec)





segundos = 1324

segundos_para_minuto = 60

minutos = 0

horas = 0

# while segundos > segundos_para_minuto:

if segundos >= 60:
    print(f'00:00:{segundos_para_minuto - 60}')
    minutos += 1
    print(f'00:{minutos}:{segundos_para_minuto - 60}')
    
