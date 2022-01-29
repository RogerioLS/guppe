"""
POO - Atributos

Em Python, dividimos os atributos em 3 grupos
    - Atributos de Instâncias;
    - Atributos de Classe;
    - Atributos Dinâmicos;

Atributos de instância: São atributos declarados dentro do metodo construtor.

"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Acesso:
    """ Quando colocamos self.__ quer dizer que nosso atributo é privado """
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Exemplo

user = Acesso('user@gmail.com', '123')
print(user.email)
user.mostra_email()
user.mostra_senha()
