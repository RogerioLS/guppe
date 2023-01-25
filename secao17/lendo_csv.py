"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separados por virgula
1,2,3,4,
"oi", "ola", "python"

# Possível de se trabalhar, mas não é o ideal (trabalhoso)
with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',')[3:]
    print(dados)
"""

# Reader
from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')
    next(leitor_csv)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')

print('-------------------------------')

# DictReader
from csv import DictReader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    next(leitor_csv)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]}')

