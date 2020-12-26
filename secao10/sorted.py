"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudadmos em Lista
o sorted só funciona em lista.

Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo

numeros = {6, 4, 7, 2 ,8 ,0}
print(numeros)
print(sorted(numeros)) # Ordena do menor para o maior
print(numeros)

numeros = [2, 1, 6, 3, 7, 4, 0]
print(numeros)
print(sorted(numeros))

# Adicionando parametros ao sorted()
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor


"""

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'Joao', 'tweets': ['Eu quero tomar breja', 'delegado online']},
    {'username': 'Rodrigo', 'tweets': ['Eu quero tomar breja', 'Bigode']},
    {'username': 'Rogerio', 'tweets': []},
    {'username': 'Fabiana', 'tweets': []},
    {'username': 'Paulinho', 'tweets': ['Eu quero fazer uma tatto', 'tatto online']},
    {'username': 'Henrique', 'tweets': [], 'cor': 'preto'}
]

print(usuarios)

# Ordenando por username - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo número de twwets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


# ultimo exemplo
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock', 'tocou': 94}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

