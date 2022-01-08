"""
Sistema de Arquivos - Manipulação

"""
import os
import tempfile

# Descobrindo se um arquivo ou diretorio existe
print(os.path.exists('arquivo.txt'))
print(os.path.exists('arquivo.txt'))

# Diretório
print(os.path.exists('geek'))
print(os.path.exists('outro'))

# Criando arquivos
os.mknod('arquivo-teste.txt')
os.mknod('C:\\Users\\Rogerio Lopes\\PycharmProjects\\guppe\\arquivo_teste_ca.txt')

# Criando diretório
os.mkdir('exemplo')

# Criando multiplos diretorios
os.makedirs('templates/geek/university', exist_ok=True)

# Renomear arquivos e diretórios
os.rename('templates/geek/university', 'templates/geek/university2')

# Como deletar arquivos
os.remove('arquivo-teste.txt')

# Como remover diretorios
os.rmdir('templates/geek/university')

# Removendo uma árvore de arquivos
for arquivo in os.scandir('templates/geek/university'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Removendo uma árvore de diretórios
os.removedirs('templates/geek/university')

# Trabalhando com arquivos e diretorios temporarios
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Criando um arquivo tempório
with tempfile.TemporaryDirectory() as tmp:
    tmp.write(b'Rogerio\n') # b é por conta que em um arquivo temporario so podemos escrever em bits
    tmp.seek(0)
    print(tmp.read())
