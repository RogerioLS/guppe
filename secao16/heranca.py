"""
POO - Herança(Inheritance)

A ideia de herança é a de reaproveitar código.Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

* Quando uma classe herda de outra classe ela herda TODOS os atributos e metodos da classe herdada
* Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe:
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;
* Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

* Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe
em classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        # Não é comum passar o nome da classe como heranca
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda


class Funcionarios(Pessoa):
    """Funcionario herda de pessoa"""

    def __init__(self, nome, sbrenome, cpf, matricula):
        # Forma comum
        super().__init__(nome, sbrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self.__Pessoa_cpf)
        return f'Funcionario: {self.__matricula} Nome: {self.__Pessoa__nome}'


cliente = Cliente('Rogerio', 'Lopes', '123.465.789.00', 5000)

print(cliente.nome_completo())
print(cliente.__dict__)
