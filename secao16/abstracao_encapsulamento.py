"""
POO - Abstração e Encapsulamento
O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando
Classes.

Encapsular

          Classes
---------------------------
/                         /
/   atributos e metodos   /
/_________________________/

# Relembrando Atributos/Médotos privados em Python

Imagina que temos uma classe chamada Pessoa,contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

Exemplo -Acessando elementos privados fora da classe:

Instancia._Pessoa__nome
Instancia._Pessoa__falar()

Abstração, em POO é o ato de expor apenas dados relevantes de um classe, escondendo atributos e métodos
privados de usuário.
"""


class Conta:

    contador = 400
    """Atributos privados"""
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    """Metodos publicos"""
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    """Metodos"""
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    """Metodos"""
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')
    """Metodos"""
    def transferir(self, valor, conta_destino):
        """1 - Remove o valor da conta de origem"""
        self.__saldo -= valor
        """Taxa de transferencia paga por quem realizou a transferencia"""
        self.__saldo -= 10

        """2 - Adiciona o valor na conta de destino"""
        conta_destino.__saldo += valor


# Testando

conta1 = Conta('rogerio', 150.00, 1500)
conta1.extrato()

conta2 = Conta('rogerio2', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()
