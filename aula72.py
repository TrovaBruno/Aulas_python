# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao (*args):
    total = 1 
    for numero in args:
        total *= numero
    return total

multiplicar = multiplicacao(1,2,3,4,5)
print(multiplicar)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    # else:
    #     return f'{numero} é impar' PODEMOS FAZER ASSIM OU:
    return f'{numero} é impar' # SEM O ELSE

print(par_impar(2))
print(par_impar(3))
print(par_impar(4))

