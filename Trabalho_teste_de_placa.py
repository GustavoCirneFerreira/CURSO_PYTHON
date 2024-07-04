import random
import string
import re
import sys

 

def gerar_letras(qtd):

    return ''.join(random.choices(string.ascii_uppercase, k=qtd))

 

def gerar_numeros(qtd):

    return ''.join(random.choices(string.digits, k=qtd))

 

def gerar_placa_mercosul():

    letras = gerar_letras(3)

    numeros1 = gerar_numeros(1)

    letras_meio = gerar_letras(1)

    numeros2 = gerar_numeros(2)

    return f"{letras}{numeros1}{letras_meio}{numeros2}"



def gerar_base_dados_placas(qtd_registros):

    base_dados = set()

    while len(base_dados) < qtd_registros:

        base_dados.add(gerar_placa_mercosul())

    return list(base_dados)



def verificar_formato_placa(placa):

    padrao = re.compile(r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$')

    return bool(padrao.match(placa))

 

def testar_base_dados(base_dados):

    registros_validos = 0

    registros_invalidos = 0

    placas_invalidas = []

   

    for placa in base_dados:

        if verificar_formato_placa(placa):

            registros_validos += 1

        else:

            registros_invalidos += 1

            placas_invalidas.append(placa)

   

    # Verificar duplicatas

    duplicatas = len(base_dados) - len(set(base_dados))

   

    return {

        "total_registros": len(base_dados),

        "registros_validos": registros_validos,

        "registros_invalidos": registros_invalidos,

        "placas_invalidas": placas_invalidas,

        "duplicatas": duplicatas

    }

#<--------------------------------------------------------------------->

def gerar_renainf():

    renainf = 'LLLLLLLLLL'

    return renainf 



def gerar_base_dados_renainf(qtd_registros):

    base_dados = []

    while len(base_dados) < qtd_registros:

        base_dados.append(gerar_renainf())

    return list(base_dados)



def testar_base_dados_renainf(base_dados):

    registros_validos_renainf = 0

    registros_invalidos_renainf = 0

    renainf_invalidos = []


    for renainf in base_dados:

        if renainf.isdigit() and len(renainf) == 10:

            registros_validos_renainf += 1

        else:

            registros_invalidos_renainf += 1

            renainf_invalidos.append(renainf)

    

    # Verificar duplicatas:

    duplicatas = len(base_dados) - len(set(base_dados))


    return {

        "total_registros": len(base_dados),

        "registros_validos": registros_validos_renainf,

        "registros_invalidos": registros_invalidos_renainf,

        "renainf_invalidos": renainf_invalidos,

        "duplicatas": duplicatas

    }

#<--------------------------------------------------------------------->

def gerar_orgao_autuador():

    lista_de_autuadores = ['DETRAN-PE', 'PRF', 'BPTran',
                            'DER-PE', 'CTTU', 'AMT', 'PREF RECIFE']
    
    autuador = random.choice(lista_de_autuadores)

    codigo = gerar_numeros(6)

    orgao_autuador = f'{codigo} - {autuador}'

    return orgao_autuador



def gerar_base_dados_orgao_autuador(qtd_registros):

    base_dados = set()

    while len(base_dados) < qtd_registros:

        base_dados.add(gerar_orgao_autuador())

    return list(base_dados)



def testar_base_dados_orgao_autuador(base_dados):

    lista_de_validação_de_autuadores = ['DETRAN-PE', 'PRF', 'BPTran',
                                         'DER-PE', 'CTTU', 'AMT', 'PREF RECIFE']
    
    registros_orgaos_autuadores_validos = 0

    registros_orgaos_autuadores_invalidos = 0

    orgaos_autuadores_invalidos = []


    for orgao_autuador in base_dados:

        if ' - ' not in orgao_autuador:

            registros_orgaos_autuadores_invalidos += 1

            orgaos_autuadores_invalidos.append(orgao_autuador)

            continue
        
        # Encontre a posição do " - "
        pos_hifen = orgao_autuador.find(' - ')
        
        codigo = orgao_autuador[:pos_hifen]

        orgao = orgao_autuador[pos_hifen + 3:]

        
        if len(codigo) != 6 or not codigo.isdigit():

            registros_orgaos_autuadores_invalidos += 1

            orgaos_autuadores_invalidos.append(orgao_autuador)

            continue
        
        if orgao not in lista_de_validação_de_autuadores:

            registros_orgaos_autuadores_invalidos += 1

            orgaos_autuadores_invalidos.append(orgao_autuador)
            
            continue
        
        registros_orgaos_autuadores_validos += 1


    duplicatas = len(base_dados) - len(set(base_dados))

    resultado = {
        'total_registros': len(base_dados),
        
        'registros_validos': registros_orgaos_autuadores_validos,

        'registros_invalidos': registros_orgaos_autuadores_invalidos,

        'orgaos_autuadores_invalidos': orgaos_autuadores_invalidos,

        'duplicatas': duplicatas

    }

    return resultado
    
#<--------------------------------------------------------------------->

def gerador_data_de_cometimento():

    limite_dia = 31

    limite_mes = 12

    limite_ano = 2024

    inicio_ano = 1980

    inicio_dia_mes = 1

    

    dia = random.randint(inicio_dia_mes, limite_dia)

    mes = random.randint(inicio_dia_mes, limite_mes)

    ano = random.randint(inicio_ano, limite_ano)


    dia_formatado = '{:02d}'.format(dia)

    mes_formatado = '{:02d}'.format(mes)

    return f'{dia_formatado}/{mes_formatado}/{ano}'



def gerar_base_dados_data_de_cometimento(qtd_registros):

    banco_dados = set()

    while len(banco_dados) < qtd_registros:

        banco_dados.add(gerador_data_de_cometimento())

    return list(banco_dados)



def verificar_formato_data(data):

    padrao = re.compile(r'^[0-9]{2}[/][0-9]{2}[/][0-9]{4}$')

    return bool(padrao.match(data))



def testar_base_dados_data_de_cometimento(base_dados):

    registros_validos_data = 0

    registros_invalidos_data = 0

    datas_invalidas = []


    for data in base_dados:

        if verificar_formato_data(data):

            registros_validos_data += 1

        else:

            registros_invalidos_data += 1

            datas_invalidas.append(data)

    # Verificar duplicatas:

    duplicatas = len(base_dados) - len(set(base_dados))


    return {

    "total_registros": len(base_dados),

    "registros_validos": registros_validos_data,

    "registros_invalidos": registros_invalidos_data,

    "datas_invalidas": datas_invalidas,

    "duplicatas": duplicatas

    }

#<--------------------------------------------------------------------->

def gerar_auto_de_infração():

    letras = gerar_letras(2)

    numeros = gerar_numeros(8)

    return f'{letras}{numeros}'



def gerar_base_dados_auto_infracao(qtd_registros):

    base_dados = set()

    while len(base_dados) < qtd_registros:

        base_dados.add(gerar_auto_de_infração())

    return list(base_dados)



def verificar_formato_auto_infracao(infracao):

    padrao = re.compile(r'^[A-Z]{2}[0-9]{8}$')

    return bool(padrao.match(infracao))



def testar_base_dados_auto_infracao(base_dados):

    registros_validos_infracao = 0

    registros_invalidos_infracao = 0

    infracoes_invalidas = []


    for infracao in base_dados:

        if verificar_formato_auto_infracao(infracao):

            registros_validos_infracao += 1

        else:

            registros_invalidos_infracao += 1

            infracoes_invalidas.append(infracao)

    
    # Verificar duplicatas:

    duplicatas = len(base_dados) - len(set(base_dados))


    return {

    "total_registros": len(base_dados),

    "registros_validos": registros_validos_infracao,

    "registros_invalidos": registros_invalidos_infracao,

    "infracoes_invalidas": infracoes_invalidas,

    "duplicatas": duplicatas

    }

#<--------------------------------------------------------------------->

def gerar_codigo_infracao():

    codigo = random.randint(180, 181)

    return f'{codigo}'



def gerar_base_dados_codigo_infracao(qtd_registros):

    base_dados = []

    while len(base_dados) < qtd_registros:

        base_dados.append(gerar_codigo_infracao())

    return list(base_dados)



def testar_base_dados_codigo_infracao(base_dados):

    registros_validos_codigo = 0

    registros_invalidos_codigo = 0

    codigos_invalidos = []


    for codigo in base_dados:

        if codigo == '180' or codigo == '181' and codigo.isdigit():

            registros_validos_codigo += 1

        else:

            registros_invalidos_codigo += 1

            codigos_invalidos.append(codigo)


    # Verificar duplicatas:

    duplicatas = len(base_dados) - len(set(base_dados))


    return {

    "total_registros": len(base_dados),

    "registros_validos": registros_validos_codigo,

    "registros_invalidos": registros_invalidos_codigo,

    "codigos_invalidos": codigos_invalidos,

    "duplicatas": duplicatas

    }

# <------------------------------ RESULTADOS --------------------------------->

# PLACAS MERCOSUL:
# Gerar uma base de dados com 20 registros de placas no padrão Mercosul

base_dados_placas = gerar_base_dados_placas(20)

# Testar a base de dados

resultados_teste = testar_base_dados(base_dados_placas)

# <------------------------------------------------------------------------->

# CÓDIGOS RENAINF:
# Gerar uma base de dados com 20 registros de infrações RENAINF

base_dados_renainf = gerar_base_dados_renainf(20)

# Testar os dados RENAINF

resultados_teste_renainf = testar_base_dados_renainf(base_dados_renainf)

# <------------------------------------------------------------------------->

# ORGÃOS AUTUADORES:
# Gerar uma base dados com 20 registros dos orgãos autuadores das placas:

base_dados_orgao_atuador = gerar_base_dados_orgao_autuador(20)

# Testar os dados dos orgãos:

resultados_teste_orgao_autuador = testar_base_dados_orgao_autuador(base_dados_orgao_atuador)

# <------------------------------------------------------------------------->

# DATAS DE COMETIMENTO:
# Gerar uma base de dados com 20 registros das datas de cometimento:

base_dados_datas_de_cometimento = gerar_base_dados_data_de_cometimento(20)

# Testar os dados das datas:

resultados_teste_datas_de_cometimento = testar_base_dados_data_de_cometimento(base_dados_datas_de_cometimento)

# <------------------------------------------------------------------------->

# AUTOS DE INFRAÇÕES:
# Gerar uma base de dados com 20 registros dos autos de infração:

base_dados_auto_infracao = gerar_base_dados_auto_infracao(20)

# Testas os dados das infrações:

resultados_teste_auto_infracao = testar_base_dados_auto_infracao(base_dados_auto_infracao)

# <------------------------------------------------------------------------->

# CÓDIGOS DE INFRAÇÕES:
# Gerar uma base de dados com 20 registros dos codigos de infração:

base_dados_codigo_infracao = gerar_base_dados_codigo_infracao(20)

# Testar os dados dos codigos:

resultados_teste_codigo_infracao = testar_base_dados_codigo_infracao(base_dados_codigo_infracao)

# <------------------------------------------------------------------------->

print('RESULTADO DAS PLACAS:')

print()

print(f"Total de Registros: {resultados_teste['total_registros']}")

print(f"Registros Válidos: {resultados_teste['registros_validos']}")

print(f"Registros Inválidos: {resultados_teste['registros_invalidos']}")


if resultados_teste['registros_invalidos'] > 0:

    print("Placas Inválidas:")

    for placa in resultados_teste['placas_invalidas']:

        print(placa)

print(f"Duplicatas: {resultados_teste['duplicatas']}")


# RESULTADOS RENAINF:

print('<------------------------------>')

print('RESULTADO RENAINF:')

print()

print(f"Total de Registros: {resultados_teste_renainf['total_registros']}")

print(f"Registros Válidos: {resultados_teste_renainf['registros_validos']}")

print(f"Registros Inválidos: {resultados_teste_renainf['registros_invalidos']}")


if resultados_teste_renainf['registros_invalidos'] > 0:

    print("Códigos RENAINF Inválidos:")

    for renainf in resultados_teste_renainf['renainf_invalidos']:

        print(renainf)

print(f'Duplicatas: {resultados_teste_renainf['duplicatas']}')


# RESULTADOS ORGÃOS AUTUADORES:

print('<------------------------------>')

print('RESULTADO ORGÃOS AUTUADORES:')

print()

print(f"Total de Registros: {resultados_teste_orgao_autuador['total_registros']}")

print(f"Registros Válidos: {resultados_teste_orgao_autuador['registros_validos']}")

print(f"Registros Inválidos: {resultados_teste_orgao_autuador['registros_invalidos']}")


if resultados_teste_orgao_autuador['registros_invalidos'] > 0:

    print('Orgãos Autuadores Inválidos:')

    for orgao_autuador in resultados_teste_orgao_autuador['orgaos_autuadores_invalidos']:

        print(orgao_autuador)

print(f'Duplicatas: {resultados_teste_orgao_autuador['duplicatas']}')


# RESULTADOS DAS DATAS DE COMETIMENTO:

print('<------------------------------>')

print('RESULTADO DAS DATAS DE COMETIMENTO:')

print()

print(f"Total de Registros: {resultados_teste_datas_de_cometimento['total_registros']}")

print(f"Registros Válidos: {resultados_teste_datas_de_cometimento['registros_validos']}")

print(f"Registros Inválidos: {resultados_teste_datas_de_cometimento['registros_invalidos']}")


if resultados_teste_datas_de_cometimento['registros_invalidos'] > 0:

    print('Datas de Cometimento Inválidas:')

    for data in resultados_teste_datas_de_cometimento['datas_invalidas']:

        print(data)

print(f'Duplicatas: {resultados_teste_datas_de_cometimento['duplicatas']}')


# RESULTADO AUTO DE INFRAÇÃO:

print('<------------------------------>')

print('RESULTADO DOS AUTOS DE INFRAÇÃO:')

print()

print(f"Total de Registros: {resultados_teste_auto_infracao['total_registros']}")

print(f"Registros Válidos: {resultados_teste_auto_infracao['registros_validos']}")

print(f"Registros Inválidos: {resultados_teste_auto_infracao['registros_invalidos']}")


if resultados_teste_auto_infracao['registros_invalidos'] > 0:

    print('Autos de Infrações Inválidas:')

    for infracao in resultados_teste_auto_infracao['infracoes_invalidas']:

        print(infracao)

print(f'Duplicatas: {resultados_teste_auto_infracao['duplicatas']}')


# RESULTADO CÓDIGO DE INFRAÇÃO:

print('<------------------------------>')

print('RESULTADO DOS CÓDIGOS DE INFRAÇÃO:')

print()

print(f"Total de Registros: {resultados_teste_codigo_infracao['total_registros']}")

print(f"Registros Válidos: {resultados_teste_codigo_infracao['registros_validos']}")

print(f"Registros Inválidos: {resultados_teste_codigo_infracao['registros_invalidos']}")



if resultados_teste_codigo_infracao['registros_invalidos'] > 0:

    print('Códigos de Infração Inválidos:')

    for codigo in resultados_teste_codigo_infracao['codigos_invalidos']:

        print(codigo)

print(f'Duplicatas: {resultados_teste_codigo_infracao['duplicatas']}')