"""
POO - Propriedades - Properties

* Em linguagem de programação como o Java, ao declararmos atríbutos privados nas classes,
costumamos a criar métodos públicos para manipulação desses atríbutos. Esses métodos são
conhecidos por gatters e setters, onde os getters retornam o valor do atributo e os setters
alteram o valor do mesmo.

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite


conta1 = Conta('Teste1', 3000, 5000)
conta2 = Conta('Teste2', 4000, 6000)

print(conta1.extrato())
print(conta2.extrato())

#soma = conta1._Conta__saldo + conta2._Conta__saldo
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldos das contas é {soma}')
