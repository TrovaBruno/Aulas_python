"""
Fatiamento de strings
012345678
Olá mundo
-987654321

Fatiamento [i:f:p] [::]
inicio:fim:passo(de 1 em 1 é o padrão)

obs: a função len retorna a qtd de carcateres da str

"""

variavel = 'Ola mundo'
print(variavel[4:]) # colocando os dois pontos ele vai até o final 
print(variavel[0:5]) # colocando dessa forma ele vai do item 0 até o 4, visto que ele omite o ultimo

print(len(variavel)) # conta a qtd de caracter
print(len(variavel[2])) # conta a qtd de no item 2


