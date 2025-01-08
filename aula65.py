"""
Introdução as funções (def) em Python
Funçõs são trechos de código usados para 
replicar determinadas ação ao longo do seu código
Elas podem receber valores para parâmentros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""
def saudacao (nome = 'Sem nome'):
    print (f'Olá, {nome}!')

saudacao('Bruno')
saudacao('Geovana')
saudacao()