"""
Map

Com Map, fazemos mapamento de valores para função
"""

import math


def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(5))
print(area(3.5))


raios = [2, 4, 6, 7, 9]


#Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

#Forma 2 - map

#Map é uma função que recebe dois parametros: O primeiro a função, o segundo um iterável. Retorna um map object


areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

#Forma 3 - Map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

#OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera


# Mais um exeplo
cidades = [('São Paulo', 22), ('Ceara', 30), ('Rio de Janeiro', 32), ('Bahia', 35), ('Manaus', 19)]
print(cidades)

# formula para transforma graus em farenaits "f = 9/5 * c + 32"
# Lamba

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))











