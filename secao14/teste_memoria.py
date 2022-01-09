"""
Teste de memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 11
"""


def fib_lista(ma):
    """ Função usando Listas Utilizou 449MB de memoria pra rodar um for de 100000 """
    nums = []
    a, b = 0, 1
    while len(nums) < ma:
        nums.append(b)
        a, b = b, a + b
    return nums


def fib_gen(ma):
    """ Função usando Listas Utilizou 3MB de memoria pra rodar um for de 100000 """
    a, b, contador = 0, 1, 0
    while contador < ma:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Testando
for n in fib_gen(100000):
    print(n)
