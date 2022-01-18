"""
Preservando metadatas com wraps

Metadatas -> São dados intrisecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades

"""

# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma(10, 30))
print(soma.__name__)  # ao chamar essas funçõs como retorno nos devolve a função
print(soma.__doc__)  # a funcao logar e está errado esse metodo.

# Resolução do Problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma(10, 30))
print(soma.__name__)  # ao chamar essas funçõs como retorno nos devolve a função
print(soma.__doc__)
print(help(soma))
