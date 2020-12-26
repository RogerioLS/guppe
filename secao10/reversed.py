"""
Reversed

OBS: Não confunda com a função reserve() que estudaddos nas listas.

A função reverse() só funciona em lista.

Já a função reversed() funciona com qualquer iteravel.

Sua função é inverter o iteravel.

"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla, ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto (Set) em conjuntos não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Rogerio Lopes'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Rogerio Lopes'))))

# Já vimos como fazer isso mais facil com o slice de string
print('Rogerio Lopes'[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n, end='')

print('\n')

# Apesar que também já vimos como fazer isso utilizando o proprio range()
for n in range(9, -1, -1):
    print(n, end='')