def CalculoCPF():
# REMOVING INVALID STRINGS TO CONVERT TO INTEGER:
# 1ST STEP: REMOVING THE DASH SIGN:

    cpf_str = '746.824.890-70'
    remove_traço = cpf_str.split('-')

    remove_70 = remove_traço[0] # REMOVING THE LAST TWO NUMBERS TO MAKE THE CPF CALCULATION:
    cpf_sem_traço =  ''.join(remove_70) #  JOINING THE LIST TO MAKE A STRING WITHOUT THE DASH SIGN:

# REDO THE SAME STEP FOR REMOVING DE DASH SIGN
# 2ND STEP: REMOVING THE DOT SIGN:

    remove_ponto = cpf_sem_traço.split('.')
    cpf_str = ''.join(remove_ponto) #  JOINING THE LIST TO MAKE A STRING:

# 3RD STEP: TRANSFORMING THE STRING TO INTEGER TO START THE CALCULATION
# USING FOR:

    lista_calculo_cpf = []  # MAKING A LIST TO CONTAIN EVERY NUMBER IN THE CPF 
    mult = 10

    for numero_str in cpf_str:  # USING FOR TO MULTIPLY EVERY SINGLE INDIVIDUAL NUMBER:
        numero_int = int(numero_str) * mult
        mult -= 1
        lista_calculo_cpf.append(numero_int)
    # output: [70, 36, 48, 56, 12, 20, 32, 27, 0]

# 4TH STEP: SUM ALL THE NUMBERS FROM THE LIST AND MULTIPLY IT BY 10 AND
# CALCULATE THE DIVISION REMAINDER OF 11:
    
    cpf_sum = sum(lista_calculo_cpf)
    cpf_mult = cpf_sum * 10
    cpf_remainder = cpf_mult % 11
    # output: 7

# 5TH STEP: CHECK IF THE RESULT IS OVER OR LESS THAN 9:
    if cpf_remainder > 9:
        return 0
    else:
        return cpf_remainder

print(CalculoCPF())
