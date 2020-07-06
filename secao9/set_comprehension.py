"""
Set comprehension

lista = [1, 2, 3, 4, 5}
set = {1, 2, 3, 4, 5}

"""

# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplos outro
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Exmplos gerando chaves
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Com String
letras = {letra for letra in 'Geek University'}
print(letras)
print()