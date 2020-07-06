"""
Listas aninhas (nested list)

- Algumas linguagens com (C/JAVA) possuem uma estrutura de dados chamada ARRAY
    - Unidimencional (ARRAY/VETORES)
    - Multidimencionais (matrizes)

Em python nós temos as listas

numeros = [1, 'b', [2,3,4,5], 'Olá mundo']

print(listas)
print(type(listas))

# Como fazemos para acessar os dados

print(listas[0][2])
print(listas[-2][-2])


# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #3 x 3

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]


"""

# Outros exemplos
# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)]for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])


