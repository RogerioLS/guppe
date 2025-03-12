"""
Doctests

Docstests são testes que colocamos na docstring das funções/métodos  Python.
Execute `python -m doctest -v doctests.py` no seu terminal pra rodar o test

26:01 

"""

# Tipo doctest
def soma(a, b):
    """soma os numeros a e b
    
    >>> soma(1, 2)
    3
    """
    return a + b

# Tipo TDD
def duplicar(valores):
    """duplica os valores em uma lista
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

# Erro inesperado
# OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Tem que ser aspas simples.
def fala_oi():
    """Fala oi
    
    >>> fala_oi()
    'oi'
    """
    return 'oi'


