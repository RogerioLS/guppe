"""
Leitura de Arquivo

Para o conteudo de um arquivo em python, utilizamos a função integrada open()
que literalmente significa 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função retorna
um _io. TextIOWrapper e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFounderError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Modo de Leitura. r -> read() -> ler

"""

# Exemplo

arquivo = open("texto.txt")
print(arquivo)
print(type(arquivo))
# A função read lê todo o conteudo e não linha a linha
print(arquivo.read())
# print(arquivo.read(50))
