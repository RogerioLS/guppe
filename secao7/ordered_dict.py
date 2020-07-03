"""
Modulo collections : Ordered Dict



# em um dicionario a ondem de inserção dos elementos nao é garantido
dicionario = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')



from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b':2, 'c':3, 'd':4, 'e':5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:vlaor={valor}')



"""

from collections import OrderedDict
# entendendo a diferença entre Dict e Ordered Dict
# dicionarios comuns

dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}
print(dict1 == dict2) # True -> já que as ordem dos elementos nao importa para dicionario

# ordered Dict

odict1 = OrderedDict({'a':1, 'b':2})
odict2 = OrderedDict({'b':2, 'a':1})
print(odict1 == odict2) # False -> já que a ordem dos elementos importa para o OrderedDict
