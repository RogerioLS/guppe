"""
Modulo Collections - Default Dict



dicionario = {'curso': 'Promação em python'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # Key erro

Default Dict -> Ao criar um dicionario utilizando-d, nó informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definifo. Caso tentemos acessar uma chave que não existe, essa cheva será


OBS: lambdas são funcoes sem nome que podem ounnão receber parametros de entrada
e retornar valores.

"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro']) # KeyError no dicionario comum, mas aqui não.
print(dicionario)
