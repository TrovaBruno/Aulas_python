# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor):
        self._cor = cor  # Usando um atributo privado com o prefixo '_'

    @property
    def cor(self):
        print("SEGUE")
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor

caneta = Caneta('Azul')
print(caneta.cor)  # Deve imprimir 'SEGUE' e 'Azul'
caneta.cor = 'Vermelha'
print(caneta.cor) 