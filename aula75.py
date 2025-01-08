# Exercícios
# Crie funções que duplicam, triblicam e quadruplicam 
# o numero recebido como parâmetro

# def multiplicacao(numero, multiplica):
#     return numero ** multiplica

# print(multiplicacao(2,3))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))