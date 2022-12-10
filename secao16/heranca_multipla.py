"""
POO - Herança Mútipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

#OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivacao Direta:
    - Por Multiderivacao Indireta:


# Exemplo 1 - Multiderivacao Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivacao Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass

#OBS: Não importa se a derivacao é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e metodos das super classes.

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimento(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimento(self):
        return f'Eu sou {self._Animal__nome} do terra'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimento())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimento())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimento()) # ???

# Objeto é instância de...
print(f'Tux é instância de Animal {isinstance(tux, Animal)}')
print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de objeto? {isinstance(tux, object)}')
