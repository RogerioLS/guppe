"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivo do sistema operacional, precisamos importar
e fazer uso do modulo os.

os -> Operating System.
"""

# Fazer o import
import os

# getcwd() -> pega o current work director -> diretorio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretorio, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretorio é absoluto ou relativo
print(os.path.isabs('/home/geek/')) # False
print(os.path.isabs('C:\\Users\\geek')) # Para windows

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

# Podemo listar os arquivo e diretorios com o lisdir()
print(len(os.listdir()))
print(os.listdir())
