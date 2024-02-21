import re
import sys

def CalculoCPF():
# REMOVING INVALID STRINGS TO CONVERT TO INTEGER:
# 1ST STEP: REMOVING THE DASH SIGN:
    
    cpf = '257.218.597-09'.replace('.', '').replace('-' , '') #  MORE CORRECT SOLUTION
    remove_traço = cpf.split('-')
    cpf_sem_traço =  ''.join(remove_traço)

# REDO THE SAME STEP FOR REMOVING DE DASH SIGN
# 2ND STEP: REMOVING THE DOT SIGN:

    remove_ponto = cpf_sem_traço.split('.')
    cpf_sem_ponto = ''.join(remove_ponto)
    cpf_str_9_digitos= cpf_sem_ponto[:9]

# 3RD STEP: TRANSFORMING THE STRING TO INTEGER TO START THE CALCULATION
# USING FOR:

    lista_calculo_cpf_digito_1 = []  # MAKING A LIST TO CONTAIN EVERY NUMBER IN THE CPF 
    mult_digito_1 = 10

    for numero in cpf_str_9_digitos:  # USING FOR TO MULTIPLY EVERY SINGLE INDIVIDUAL NUMBER:
        numero_int_1 = int(numero) * mult_digito_1
        mult_digito_1 -= 1
        lista_calculo_cpf_digito_1.append(numero_int_1)

# 4TH STEP: SUM ALL THE NUMBERS FROM THE LIST AND MULTIPLY IT BY 10 AND
# CALCULATE THE DIVISION REMAINDER OF 11:
    
    cpf_digito_1 = (sum(lista_calculo_cpf_digito_1) * 10) % 11
    # output: 7

# 5TH STEP: CHECK IF THE RESULT IS OVER OR LESS THAN 9:

    cpf_digito_1 = cpf_digito_1 if cpf_digito_1 <= 9 else 0
# <------------------------------------------------------------------------->
    
# 6TH STEP: CALCULATING THE LAST NUMBER OF THE CPF(746.824.890-7(0) <- THIS ONE):
# EXACT SAME STEPS FROM BEFORE, NOW WITH THE PENULTIMATE NUMBER ON IT:
    
    cpf_str_10_digitos = cpf_sem_ponto[:10]

    lista_calculo_cpf_digito_2 = []
    mult_digito_2 = 11

    for numero in cpf_str_10_digitos:
        numero_int_2 = int(numero) * mult_digito_2
        mult_digito_2 -= 1
        lista_calculo_cpf_digito_2.append(numero_int_2)

    cpf_digito_2 = (sum(lista_calculo_cpf_digito_2) * 10) % 11
    cpf_digito_2 = cpf_digito_2 if cpf_digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = (f'{cpf_str_9_digitos}{cpf_digito_1}{cpf_digito_2}')
    print(cpf_gerado_pelo_calculo)

    if cpf_gerado_pelo_calculo == cpf_sem_ponto:
        print('O seu CPF é válido!')
    else:
        print('O seu CPF não é válido!')
    

CalculoCPF()
