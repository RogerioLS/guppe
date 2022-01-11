"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que retorna outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso
"""

# Exemplo - Defininfo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

"""
Nested Functions - Funções Aninhadas
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
Ou também Inner Functions (Funções Internas)
"""

# Exmplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


# Testando
print(cumprimento('Angelina'))
print(cumprimento('Felicity'))

# Retornando funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahahah', 'kkkkkkkkkkkk', 'ayyayayayayayayay'))
    return rir()


# Testando
rindo = faz_me_rir()
print(rindo)

"""
Inner Functions (Funções Internas/Nested Functions) podem acessar o escopo de funções mais externas
"""


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahaha', 'lolololololol', 'kkkkkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada()


# Testando
ri = faz_me_rir_novamente('Fernanda')
print(ri)
print(ri)
print(ri)
