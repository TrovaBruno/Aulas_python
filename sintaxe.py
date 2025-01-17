#usamos list comrehension para gerar um iterável a partir de um iterável

numeros = [1, 2, 3, 4, 5]
novos_numero = [numero for numero in numeros]

numeros[0] = 20 
print(novos_numero)
print(numeros)