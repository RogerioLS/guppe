"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Metodos de instância
e Metodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

OBS: todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline

OBS: Os métodos/funções dunder em Python são chamddos de métodos mágicos

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder (underline no inicio e no fim)
não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas de linguagem. Então, evite ao máximo. De preferencia nunca faça.
"""


class Lampanda:

    def __init__(self, cor, voltagem, luminosidada):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidada
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as sha


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        """Métodos de classe"""
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'Ux344'

    def __init__(self, nome, sobrenome, email, senha):
        """Métodos de instancia, que instancia o objeto criado"""
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = sha.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        """Retorna o nome completo"""
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        """Verifica se a senha cadastrada é a mesma"""
        if sha.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


p1 = Produto('Play4', 'Video Game', 2300)
print(p1.desconto(20))
print(Produto.desconto(p1, 35))

user1 = Usuario('Roberto', 'Luiz', 'robertoLuiz@.com', '1234')
user2 = Usuario('Roberta', 'Maria', 'robertaMaria@.com', '5678')
print(user1.nome_completo())
print(user2.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Conrfirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere.....')
    exit(1)

print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.chaca_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') #metodo errado de se acessar!!

user3 = Usuario('Roberta', 'Maria', 'robertaMaria@.com', '5678')
