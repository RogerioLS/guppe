""" PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python
The Zen of Python
import this
[1] - Utilize canel case para nomes de classes: Maiusculo e pule duas linahss
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variavies
def soma();
    pass


def soma_dois();
    pass


numero = 4

numero_impar = 5


[3] - Utilize 4 espaços para identação!
if 'a' in 'morango';
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em brnaco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

# Import errado
import sys. os

# Import Certo
import sys
import os

# Não há problemas em utilizar:

from types import StringType. ListType

# Caso tenha muitos imports de um pacote, recomenda-se fazer:

from types import {
    StringType,
    ListType,
    SetType,
    OutroType,
}
# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstring
# Antes de constantes ou variaveis global.

[6] - Espaços em expressões e instruções
# Não faça:
função(_algo[_1_], {_outro: 2_}_)

# Faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo_(1)

# Faça:
algo(1)

# Não faça:
dict_['chave'] = lista_[indice]

# faça:
dict['chave'] = lista[indice]

# Não faça:
x_________=1
Y_________=3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""





