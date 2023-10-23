# CONSTANTE = "VARIAVEIS" que não vão mudar
# Muitas condições no mesmo if (ruim)
#     <- Contagem de complexidade (ruim)

velocidade = 50 # Velocidade atual do carro 
local_carro = 101 # Local atual do carro

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

carro_passou_velocidade_radar = velocidade > RADAR_1 
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_passou_velocidade_radar:
    print('Carro passou da velocidade do radar')

if carro_passou_velocidade_radar and carro_multado_radar1:
    print('Carro foi multado no radar 1')

