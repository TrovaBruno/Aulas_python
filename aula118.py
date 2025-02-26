# Problema dos parametros mutáveis

def adiciona_nome (nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista 

cliente1 = adiciona_nome('luiz')
adiciona_nome('Joana', cliente1)
adiciona_nome('Bruno', cliente1)
cliente1.append('Edu')


cliente2 = adiciona_nome('helenea')
adiciona_nome('Maria', cliente2)

print(cliente1)
print(cliente2)