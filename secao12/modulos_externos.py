"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em : https://pypi.org

Pacote colorama -> É utilizado para permitir impressão de textos coloridos no terminal

from colorama import init, Fore, Back

init()
print(Fore.MAGENTA + "Rogerio Lopes")
print(Fore.BLUE + "Rogerio Lopes")
print(Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX + "Rogerio Lopes")

Pacote Python-PDF -> Gera PDF's direto na sua maquina
"""

import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
