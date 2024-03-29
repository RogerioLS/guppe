"""
POO - Propriedades - Properties

* Em linguagem de programação como o Java, ao declararmos atríbutos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atríbutos. Esses métodos são
conhecidos por gatters e setters, onde os getters retornam o valor do atributo e os setters
alteram o valor do mesmo.

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldos das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(99999)
print(conta1.__dict__)

* essa maneira vista de acima de get e set é uma maneira bem comum no java
em python vamos utilizar as PROPRIEDADES para gerenciamento disso.

- Declara a clasee
- Atributos de classe
- Construtores e seus atributos de instacia
- Property
- Metodos de intância
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Teste1', 3000, 5000)
conta2 = Conta('Teste2', 4000, 6000)

print(conta1.extrato())
print(conta2.extrato())

#soma = conta1._Conta__saldo + conta2._Conta__saldo
soma = conta1.saldo + conta2.saldo
print(f'A soma do saldos das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 789456
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)
