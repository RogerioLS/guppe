"""
Módulo Random e o que são módulos ?

- Em Python, módulo nada mais são do que outros arquivos Python

Módulo Random -> Possui vários funções para geração de números pseudo-aleatorio.
"""
# OBS: Existem duas formas de se utilizar um módulo ou função deste
# Forma 1 - Importando todo o modulo (Não recomendado).

import random

# random() -> Gera um numero pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponivél (Ficarão em Memória). Caso você quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função especifica do módulo

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())


# uniform() -> Gerar um numero pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))


# randint() -> Gera valores pseudo-aleatorios entre os valores estabelecidos.

from random import randint

# Gerador de aposta para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ') # comceça em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iteravel.
from random import choice

jogados = ['pedra', 'papel', 'tesoura']

print(choice(jogados))

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas)

