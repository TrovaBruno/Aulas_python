"""
Operadores lógicos
And (e) OR (ou) NOT (não)
And - todas as condições precisam ser verdadeiros
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
"""

senha_permitida = 'SPFC'

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')



if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrar')

else:
    print('sair')
