"""
Operadores lógicos
And (e) OR (ou) NOT (não)
OR - Qualquer condição verdadeira avalia toda expressão como verdadeira
"""

senha_permitida = 'SPFC'

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')



if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('entrar')

else:
    print('sair')