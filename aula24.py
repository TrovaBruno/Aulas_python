"""
Interpolação básica de string
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDF0123456789)
"""

nome = 'luiz'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15)) #podemos querer mais casas decimais no 
#campo do hexadecimal para isso colocariamos %04x que seria 4 casas decimais e 
#se não tiver, preencha com 0