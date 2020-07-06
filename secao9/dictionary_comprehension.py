"""

Pense no seguinte:
Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um set (conjunto)

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionario

dicionario = {'a':1, 'b':2, 'c':3}


# Sintax
{chave:valor for valor in iterável}

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# Exemplos
numeros = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

# Exemplos
chaves = 'abcdef'
valores = [1, 2, 3, 4, 5, 6]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
"""

# Exemplos com logico condicional
numeros = [1, 2, 3, 4, 5, 6]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
print()



