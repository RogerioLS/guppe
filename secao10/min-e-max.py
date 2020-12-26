"""
Min e Max

mas() -> Retorna o  maior valor em um iterável ou o maior de dosi ou mais elementos.

# Exemplos
lista = [1, 5, 6, 8, 9, 43, 65]
print(max(lista))

tupla = (1, 5, 6, 8, 9, 43, 65)
print(max(tupla))

conjunto = {1, 5, 6, 8, 9, 43, 65}
print(max(conjunto))

dicionario = {'a': 1, 'b': 5, 'c': 6, 'd': 8, 'e': 9, 'f': 43, 'g': 65}
print(max(dicionario.values()))

------------------------------------------------------------------------------------------------------------------------

# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor:'))
val2 = int(input('Informe o segundo valor:'))
print(max(val1, val2))

------------------------------------------------------------------------------------------------------------------------

print(max(4, 5, 69))
print(max('a', 'ab', 'abc'))
print('a', 'b', 'c', 'r')
print(max(2.3545, 3.5645))
print(max('Rogerio Lopes'))

----Min-----------------------------------------------------------------------------------------------------------------

min() -> Retorna o menor valor em um itrrável ou o menor de dois ou mais elementos

# Exemplos
lista = [1, 5, 6, 8, 9, 43, 65]
print(min(lista))

tupla = (1, 5, 6, 8, 9, 43, 65)
print(min(tupla))

conjunto = {1, 5, 6, 8, 9, 43, 65}
print(min(conjunto))

dicionario = {'a': 1, 'b': 5, 'c': 6, 'd': 8, 'e': 9, 'f': 43, 'g': 65}
print(min(dicionario.values()))

------------------------------------------------------------------------------------------------------------------------

# Faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor:'))
val2 = int(input('Informe o segundo valor:'))
print(min(val1, val2))

------------------------------------------------------------------------------------------------------------------------

print(min(4, 5, 69))
print(min('a', 'ab', 'abc'))
print('a', 'b', 'c', 'r')
print(min(2.3545, 3.5645))
print(min('Rogerio Lopes'))

------------------------------------------------------------------------------------------------------------------------

# Outros exemplos
nomes = ['Rogerio', 'Joao', 'Diego', 'Amanda', 'Aliny']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock', 'tocou': 94}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO: Imprima somente o título da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO: Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda?

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 999999

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])