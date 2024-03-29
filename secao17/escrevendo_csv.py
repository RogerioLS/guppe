"""
Escrevendo em arquivo CSV

reader() (leitor), writer() (escritor)

writerow() -> Escrever uma linha

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

"""

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.
from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duracao (em minutos): ')
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao': duracao})

