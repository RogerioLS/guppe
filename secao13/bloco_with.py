"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamento

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

arquivo = open('texto.txt)

"""

# O block with - Forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

print('oi')