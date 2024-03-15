def para_camel_case(plvr):
    palavra = plvr
    plvr_traco = plvr.replace('_', '-')
    plvr_dividida = plvr_traco.split('-')
    plvr_maiuscula = [palavra.capitalize() for palavra in plvr_dividida]

    plvr_final = ''.join(plvr_maiuscula)
    print(plvr_final)

para_camel_case('tulio-e_guga')