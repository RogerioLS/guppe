"""
Pacotes

Módulos -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos:

Pacote -> É um diretório contendo uma coleção de módulos:

OBS: Nas versões 2.X do python, um pacote Python deveria conter dentro dele um
arquivo chamado __init_.py

Nas versões do Python 3.x não é mais obrigatório a utilização deste arquivo, mas
normalmente ainda é utilizado para manter compatibilidade.
"""

from geek import geek_um, geek_dois
from geek.university import geek_tres, geek_quatro

print(geek_um.pi)
print(geek_um.funcao(4, 6))

print(geek_dois.curso)
print(geek_dois.funcao_dois())

print(geek_tres.funcao_tres())
print(geek_quatro.funcao_quatro())

# Podemos também fazer o import de uma função específica

from geek.geek_um import funcao

print(funcao(3, 17))

# Também podemos fazer do subpacote

from geek.university.geek_quatro import funcao_quatro

print(funcao_quatro())



