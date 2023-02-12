"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecido por empresas
(Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores)
"""
import json
import jsonpickle

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', '2340')}])
print(type(ret))
print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
#ret = jsonpickle.encode(felix)
#print(ret)

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
    print('Arquivo criado com sucesso')

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)


