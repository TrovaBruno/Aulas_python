def divisao(x, y):
    return x / y

def multiplicacao(x, y):
    return x * y

numeros = [1, 2, 3, 4, 5]
divisaotest = [divisao(numero, 2) for numero in numeros]
multiplicatest = [multiplicacao (numero, 2) for numero in numeros]

numeros[0] = 20 

print(numeros)
print(divisaotest)
print(multiplicatest)
