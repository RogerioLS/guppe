"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção



valores = 1, 2, 3, 4, 5, 6
media = (sum(valores)) / len(valores)
print(media)

---------------------------------------------------------------


# Lib para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 4.6, 0.8, 4.3, -0.3]

# Calculadno a media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')

# OBS: Assim como a funçao map(), a filter() recebe dois parametros, sendo
# uma fução e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem
# utilizados os dados de filter() eles são apagados da memoria

----------------------------------------------------------------------------

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)
res = filter(None, paises)
print(list(res))

----------------------------------------------------------------------------

# a função filter retornar true(1) or false(0)
# a função map retorna valores

----------------------------------------------------------------------------

usuarios = [
    {'username': 'Joao', 'tweets': ['Eu quero tomar breja', 'delegado online']},
    {'username': 'Rodrigo', 'tweets': ['Eu quero tomar breja', 'Bigode']},
    {'username': 'Rogerio', 'tweets': []},
    {'username': 'Fabiana', 'tweets': []},
    {'username': 'Paulinho', 'tweets': ['Eu quero fazer uma tatto', 'tatto online']},
    {'username': 'Henrique', 'tweets': []}
]

print(usuarios)

# Filtrar os usuarios que estão inativos no Twitter

# Forma1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))


print(inativos)


"""

# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar um lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 carac.

lista = list(map(lambda nome: f'Sua instrutura é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(list(lista))

