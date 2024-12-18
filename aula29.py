"""
CONSTANTE - são variaveis que não mudam
muitas condições no mesmo if - (ruim)
        <--- tab significa bloco de código dentro de bloco de código (ruim)

"""

velocidade = 60 #veloc atual do carro
local_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #veloc maxima do radar
LOCAL_1 = 100 #local onde se encontra o RADAR_1
RADAR_RANGE = 1 #A distancia em que o radar pega

veloc_carro_pass_radar = velocidade > RADAR_1
carro_passou_radar_1 =local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <=(LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and veloc_carro_pass_radar


if veloc_carro_pass_radar: 
    print('Velocidade do carro passou o radar1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar')
