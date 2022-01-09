"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ter iretado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada:

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""

# Exemplo de Iterable
nome = 'Rogerio'
numeros = [1, 2, 3, 4, 5, 6]

# Transformando em Iterator
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it2))
print(next(it2))

# Fazendo de uma forma que não precise fazer a transformação para Iterator
for letra in nome:
    print(f'{letra}')
