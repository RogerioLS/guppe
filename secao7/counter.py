"""
Módulo Collections - Countr(Contador)
Collections -> High-performance Container DateTypes

Counter -> recebe um interavel como parametro e cria um objeto do tipo Collections Counter que é parecido
com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencia desse elemento









# Realizando o import
from collections import Counter

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias





Exemplo 2
print(Counter('Geek University'))













"""


from collections import Counter

# Exemplo 3
texto = 'Texto é um conjunto de palavras e frases encadeadas que permitem interpretação e transmitem uma mensagem.' \
        ' É qualquer obra escrita em versão original e que constitui um livro ou um documento escrito. ' \
        'Um texto é uma unidade linguística de extensão superior à frase.'

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))