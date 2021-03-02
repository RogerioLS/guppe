"""
Debuggango com PDB

PDB -> Python Debugger

Bug -> Inseto

# OBS: A utilização do print() para debugar é uma pratica ruim


# Existem formas mais profissionais de se fazer esse debug, utilizando o debuger
# Em Python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando
# o PDB - Python Debuger

# Exemplo com o python


def dividir(a, b):
    try:
        return f'O resultado da divisão foi de: {int(a) / int(b)}'
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 0))


# Exemplo com o PDB - Python Debugger - Exemplo 1
# Para utilizar o Python Debugger, precisamos importar a biblioteca
# pdb e então utilizar a função set_trace()
# comando basicos com pdb

# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Rogerio'
sobrenome = 'Lopes'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Exemplo com o PDB - Python Debugger - Exemplo 2
# Para utilizar o Python Debugger, precisamos importar a biblioteca
# pdb e então utilizar a função set_trace()
# comando basicos com pdb

# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Rogerio'
sobrenome = 'Lopes'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas
# No inicio do arquivo. Por isso, ao invés de colocarmos o import do pdb no inicio do arquivo,
# Nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoçaõ.



# Exemplo com o PDB - Python Debugger - Exemplo 2
# Para utilizar o Python Debugger, precisamos importar a biblioteca
# pdb e então utilizar a função set_trace()
# A partir do python 3.7, não é mais necessário importar a biblioteca pdb
# pois o comando de debug foi incorporado como função built-in (intregada)
# chamada breakpoint()

# comando basicos com pdb

# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Rogerio'
sobrenome = 'Lopes'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# Obs: Cuidado com conflitos entre nomes de variavel e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(2, 4, 6, 8))

# como os nomes das variaveis são os mesmos dos comandos do pdb, devemos utilizar o comando
# para imprimir as variaveis. Ou seja: p nome_da_variavel.



