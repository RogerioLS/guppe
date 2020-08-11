"""
Utilizando Lambdas

Conhecidas por expressões lambdas, ou simplesmente Lambdas,
são funções sem nome, ou seja, funções anonimas.

# Função python
def funcao(x):
    return 3 + x + 1


print(funcao(4))


# Expressão Lambda
lambda x: 3 * x + 1


# Como utilizar a expressao lambda?
calc = lambda x: 3 * x + 1


print(calc(4))
print(calc(9))


# Podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


print(nome_completo(' RoGerio' , 'Lopes '))
print(nome_completo(' roGerio     ' , ' lopeS '))




# em funções Python podemos ter nenhuma ou varias entradas. Em lambdas tambem

amar = lambda: 'Como não amar Pyhthon'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x*y) ** 0.5

tres = lambda x, y, z: 3 / (1/x+1/y+1/z)

# n = lambda x1, x1, ....., xn: <expressao>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 4, 5))



# Outros exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wills', 'Leigh Brackett']


print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""


# Funcao quadratica
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x**2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)


print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 9)(4))


