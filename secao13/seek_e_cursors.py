"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo

# seek() -> A função seek() permite movimentar o cursor para qualquer posição do arquivo
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(20)
print(arquivo.read())


# readline() -> Função que lê o arquivo linha a linha
ret = arquivo.readline()
print(ret)
print(ret.split(' '))


# readlines()
linhas = arquivo.readlines()
print(len(linhas))
"""

# Passos para se trabalhar com um arquivo
# 1 - Abrir o arquivo
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo:
print(arquivo.read())
print(arquivo.close()) # False verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo:
arquivo.close()

print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError








