"""
Modulo Collections - NAmed Tupla

# Recap Tuple
tupla = (1,2,3)
print(tupla[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parametros

"""

# import
from collections import namedtuple

# Precisamos definir o nome e parametros
# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cahorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
pingo = cachorro(idade=3, raca='vira lata', nome='Pingo')
print(pingo)

print(pingo[0]) #idade
print(pingo[1]) #raca
print(pingo[2]) #nome

# Forma 2
print(pingo.idade)
print(pingo.raca)
print(pingo.nome)

print(pingo.index('vira lata'))
print(pingo.count('vira lata'))