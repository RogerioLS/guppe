"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrario teremo um TypeError.

# Exemplo de escrita -  modo 'w' - write (escrita)

with open('novo.txt', 'w') as arquivos:
    arquivos.write('Escrever dados em arquivo é muito fácil.\n')
    arquivos.write('Podemos colocar quantas linhas quisermos.\n')
    arquivos.write('Esta é a ultima linha')
"""

with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



