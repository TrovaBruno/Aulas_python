"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '       Olha só que     ,          coisa interessante'
lista_frase_crua = frase.split(',')

lista_palavras = []
for i, frase in enumerate(lista_frase_crua):
    lista_palavras.append(lista_frase_crua[i].strip()) ## o .strip corta os espaços em branco



# print(lista_frase_crua)
# print(lista_palavras)

# frases_unidas = '-'.join('abc')
# print(frases_unidas)

frases_unidas = '---------------->'.join(lista_palavras)
print(frases_unidas)