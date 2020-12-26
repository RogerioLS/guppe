"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (buil-in). Agora temos
que importar e utilizar es função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, a4, ....., an]

# E você tem uma função que recebe dois parametros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parametros: a funçao e o iteravel.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleçao e guarda o resultado.
    passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função como primeiro argumento o resultado da aplicação anterior.
No final, reduce() ira retonrar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ..), an)

"""

# Como funciona na pratica?
# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 12, 43, 6, 34, 78, 90]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parêmetros
multi = lambda x,y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)
