# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:

    def __init__(self, cor):
        self.cor = cor
        self.cor_tampa = None

    @property
    def cor (self):
        print('ESTOU NO GETTER')
        return self._cor
    
    @cor.setter

    def cor(self, valor):
        print('ESTOU NO SETTERN')
        self._cor = valor

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)

