"""
Trabalhando com Módulos Builtin (modulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|


# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando 0 *

from random import *

print(random())


# Importando todo o modulo

import random

print(random.random())


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(4, 90))

print(rdm())

"""

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(3, 60))
lista = ['Rogerio', 'Lopes']
shuffle(lista)
print(lista)
print(choice('Rogerio'))