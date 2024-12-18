"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input ('digite um número inteiro ')

if numero.isdigit():
    numero_int =int (numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'par'

    if par_impar == False:
        par_impar_texto='impar'

    print(f'o numero {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um numero inteiro')
    
