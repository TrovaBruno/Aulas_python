"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite o seu horario: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <=11:
        print(f'Bom dia {entrada}')
    elif hora >=12 and hora <=17:
        print(f'Boa tarde {entrada}')
    elif hora >=18 and hora <=23:
        print (f'Boa noite {entrada}')
    else:
        print('Não conheço essa hora')
except:
    print(' Por favor, digite apenas numeros inteiros')