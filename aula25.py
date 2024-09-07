"""
Formatação básica de strings
s - corda
d - inteiro
f - flutuador
.<número de dígitos>f
x ou X - Hexadecimal
(Característica)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Exemplo: 0>-100,.1f
Sinalizadores de conversão - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}' )
print(f'{1000.02184075:.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')