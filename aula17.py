#and:
entrada = input("Digite [E] para ENTRAR ou [S] para SAIR: ")
senha_digitada = input("Senha: ")
senha_permitida = '123456'


if (entrada == 'E' and senha_digitada == senha_permitida):
    print("Você entrou.")
else:
    print("Você saiu.")