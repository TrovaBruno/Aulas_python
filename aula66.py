"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o arugumento (valor)

É interessante usar argumentos nomeados para alterar a ordem no envio de valores para a função
Você não pode enviar argumentos posicionais após argumentos nomeados
"""

def soma (x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

soma (1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep= '-')