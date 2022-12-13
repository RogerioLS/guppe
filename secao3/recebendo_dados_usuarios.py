"""

Recebendo dados do usuário


input()-> todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos;
- Aspas simples -> 'Angelica Jolie'
- Aspas duplas -> "Angelica Jolie"
- Aspas simples triplas '''Angelica Jolie'''
- Aspas duplas triplas -> Angelica Jolei
"""

# Entrada de dados

print("Qual é seu nome?")
nome = input()  # Input -> Entrada

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' %nome')

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')
print("Qual sua idade?")
idade = input()

if int(idade) > 18:
    print('Tem a maior de idade')
elif int(idade) == 18:
    print('Idade 18 anos')
else:
    print('Tem a menor de idade')

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print('A %s tem anos' % (nome, idade))

# Exemplo de print 'moderno' 2.x
# print('A {0} tem {1} anos'.format (nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O {nome} tem {idade} anos')

"""
# int{idade} => cast
cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'O {nome} nasceu em {2022 - int(idade)}')
