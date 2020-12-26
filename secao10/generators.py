"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

# Poderiamos ter feito utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator ocupa menos recurso na memoria
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

-----------------------------------------------------------------------------------------------

# Qual é a utilidade de getsizeoof()? verifica quantidade de byte em memoria
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memoria.
print(getsizeof('Rogerio'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(92))
print(getsizeof(3493294))
print(getsizeof(True))

--------------------------------------------------------------------------------------------

"""

from sys import getsizeof

# Gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com dictionary comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'Lis: {list_comp}')
print(f'Set: {set_comp}')
print(f'Dictionary: {dic_comp}')
print(f'Generator: {gen}')
# Eu posso iterar no Generator Expression? Sim!
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

