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

# Atribuitos de instancias, significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '789012')

user1.mostra_email()
user2.mostra_email()

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do construtos. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instâncias da classe, Ou seja, ao inves de cada instancoa da classe ter seus proprios
# valores como é o caso dos atributos de instancia, com os atributos de classe todas as instancias
# terão o mesmo valor para este atributo.


class Produto:
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Play4', 'video game', 2300)
p2 = Produto('Xbox S', 'video game', 4500)

print(p1.valor)  # modo de Acesso incorreto
print(p2.valor)

print(p2.id)

# Atributos Dinâmicos é um atributo de instancia que pode ser criado em tempo de execucao.

p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
