"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""

entrada = input (' Digite o seu nome: ')

if len(entrada) <= 4:
    print ('Seu nome é curto')

elif len(entrada) ==5:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande')
