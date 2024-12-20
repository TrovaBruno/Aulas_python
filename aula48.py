"""
Listas em python 
Tipo list - Mutavel
Suporta voleres de todos os tipos

"""

# string = 'ABCDE'

## NAVEGANDO PELOS INDICES DA MINHA LISTA E ALTERANDO ALGUM ITEM 

# #             0     1         2          3 4 
# #             -5   -4         -3       -2  -1
# lista  =    [123, True, 'Luiz Otavio', 1.2, []]
# # print(bool(lista))
# # print (lista, type(lista))
# lista[-3] = 'Maria'
# print (lista[2], type(lista [2]))




#-----------------------------------------------

## ADICIONANDO UM INDICE A MINHA LISTA E REMOVENDO UM INDICE DE MINHA LISTA

# lista = [10, 20, 30, 40]
# # lista [2] = 300
# # del lista [2]
# # print (lista)
# # print (lista[2])
# lista.append(50) ## adiciona um item ao ultimo objeto da lista
# # lista.pop() ## remove o ultimo item da lista
# # ultimo_valor = lista.pop()
# ultimo_valor = lista.pop(1)
# print(lista, 'Removido', ultimo_valor)


#-----------------------------------------------

# append - adiciona um item ao final 
# insert - adiciona um item ao indice escolhido 
# pop - remove do final ou do indice escolhido 
# del - apaga um indice
# clear - limpa a lista
# extend - estende a lista
# + - concatena a lista

# lista = [10,20,30,40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append (123)
# del lista [-1]
# lista.insert(0, 5) ## primeiro o indice e depois o valor 
# # lista.clear ()
# print(lista)

#-----------------------------------------------

# lista_a = [1,2,3]
# lista_b = [4,5,6]

# lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b) ## mexe diretamente na lista que vem antes do extend e não retorna algo para a lista_d, por isso 
# #o resultado fica 'none'.

# print (lista_d)

#-----------------------------------------------

# Cuidado com os dado mutaveis 
# = - copiado o valor (imutaveis)

# nome = 'Luiz'
# outra_variavel = nome
# nome = 'João'

# print(nome)
# print (outra_variavel)


# = - aponta para o mesmo valor na memoria (mutavel)

lista_a = ['Luiz' , 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)