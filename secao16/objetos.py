"""
POO - Objetos

Objetos -> são instancias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
nos objetos/instância de classe como variavies do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = "DESLIGADO"
        else:
            self.__ligada = "LIGADA"


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_clinte(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos
lamp1 = Lampada('branca', 110, 60)
lamp1.ligar_desligar()
lamp1.ligar_desligar()
print(f'A lâmpada está ligada?\n{lamp1.checa_lampada()}')

cli = Cliente('Eliana', '123.456.789-99')
cc = ContaCorrente(5000, 1000, cli)
print(cc.mostra_clinte())
