''' 
enumerate - enumera iteraveis (indices)
'''

lista = ["Maria", 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = list(enumerate(lista, start=19))

# print(lista_enumerada)
# print(next(lista_enumerada))

# for item in enumerate(lista):
#     indice, nome = item 
#     print(indice, nome) 

# o de cima faz a mesma coisa que o de baixo 

for indice, nome in enumerate(lista):
    print(indice, nome)