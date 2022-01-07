"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o contéudo ao final do arquivo
+ -> Abre para o modo de atualização: Leitura e Escrita.

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exita, o novo conteúdo
será adicionado ao final do arquivo. Com o modo 'a', não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open
"""
# Exemplo'x'

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2. \n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo 'a'

with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

with open('fruta.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha\n')
    arquivo.write('Mais uma linha\n')
