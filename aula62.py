"""
Calculo do SEGUNDO dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
MAIS O PRIMEIRO DIGITO
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (746824890)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <------------------ PRIMEIRO DIGITO
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0+14 = 363
Multiplicar o resultado anterior por 10
363*10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#calculo primeiro digito
#--------------------------------------------------------------
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0

for digito in nove_digitos:
    resultado +=int(digito)*contador_regressivo
    contador_regressivo -=1

digito = (resultado*10) % 11
digito = digito if digito <=9 else 0
print(digito)

#calculo segundo digito
#-----------------------------------------------------------------------
# cpf = '74682489070'
dez_digitos = nove_digitos + str(digito)
contador_regressivo_2 = 11

resultado_2 = 0
for digito2 in dez_digitos:
    resultado_2 +=int(digito2)*contador_regressivo_2
    contador_regressivo_2 -=1

digito2 = (resultado_2 * 10)%11

print(digito2)
digito2 = digito2 if digito <=9 else 0

# print(digito)
# print(dez_digitos)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito}{digito2}'
print(cpf_gerado_pelo_calculo)

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é valido')

else:
    print('CPF Inválido')