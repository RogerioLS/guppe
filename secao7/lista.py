"""
Lista em Python funcional como vatores/matrizes(arrays) em outras linguagens, com a diferença
de serem e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: Arrays
    - possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagem se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter sempre no maximo 5 valores.

Já em Python:
-Dinâminco: não possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir add elementos.
-Qualquer tipo de dado: nâo possuem tipo de dado fixo; ou seja,podemos colocar qualquer tipo de dado

type([])
lista1 = [1,21,34,53,65,76,84,46,45]
lista2 = ['G','e','e','k','','U','n','i','v','e','r','s','i','t','y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Podemos facilmente checar se determinado valor está contido na lista
num = 7
if 8 in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar um lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

Para adicionar elementos em lista, utilizando a função append
OBS: append, nós só conseguimos adicionar 1 elemento por vez
print(lista1)
lista1.append(42)
print(lista1)

# Porém você consegue add uma lista dentro de outra lista
lista1.append([1,2,3])
print(lista1)

if [1,2,3] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Coloca cada elemento na lista ao invés de uma nova lista
lista1.extend([12, 13, 14])
print(lista1)

# Podemos inserte um novo elemento na lista informando a posição do índice
# Isso não substitui o valor atual
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos juntar as listas
lista6 = lista1 + lista2
#lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos facilmente remover o ultimo elemento da lista
# OBS: o pop não somente remove o ultimo elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos á direita deste índice serão deslocados para a esquerda
# OBS: Se não houver elemento do indice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas
# Exemplo 2
curso = 'Progrmação,em,Python:'
print(curso)
curso = curso.split(',')
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando
lista6 = [1, 2, 32, True, 'Geek', 324432,]
print(lista6)
print(type(lista6))

# Iterando sobre listas
# Exemplo 1

soma =0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em lista
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0          1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como um circulos, onde
# o final de um elemento está ligado ao inicio da lista

print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3])
print(cores[-4])

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Lista aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(43)
lista.append(43)
print(lista)



# Outros métodos não importantes mas também úteis

# Encontrar o indice de um elemento na lista
numeros = [5,6,7,5,8,9,10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor9?
print(numeros.index(9))

# print(numeros.index(19)) # Gera ValueError

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError
# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer buscar dentro de um ranger, ou seja, qual indice começa a buscar
print(numero.index(5,1)) # buscando a partir do indice 1
# Caso nao tenha este elemento na lista, será apresentado erro

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8,3,6)) # Buscar indice do valor 8, entre o indice 3 a 6

# Revisão de slicing

# lista(inici:fim:passo)
# range(inici:fim:passo)

lista = [1,2,3,4]
print(lista[1:] # Iniciando no indice 1 e pegando todos os elementos restantes

#trabalhando com slice de lista com o parametro fim

print(lista[:2]) # começa em 0, pega até o índice 2 - 1
print(lista[:4]) # começa em 0, pega até o índice 4 - 1
print(lista[1:3]) # começa em 1, pega até o índice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2
print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

# Soma, Valor Max, Valor Min, Tamanho
# Se os valores forem todos inteiros ou reais

lista = [1,2,3,4,5,6]

print(sum(lista)) #soma
print(max(lista)) #MaxValor
print(min(lista)) #MinValor
print(len(lista)) #TamanhoDeLista

# Transformar uma lista em tupla

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de lista

lista = [1,2,3]
 num1, num2, num3 = lista
 print(num1)
 print(num2)
 print(num3)
# se tivermos um numero diferente da lista da-ra erro

# Copiando um lista para outra (Shallow Copy e Deep Copy)
# Forma 1

lista = [1,2,3]
print(lista)

nova = lista.copy()

print(nova)
nova.append(4)

print(lista)
print(nova)
# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas ele
# ficamos totalmente independentes, ou seja, modificando uma lista, não afeta a outra isso em Python
# é chamado de Deep Copy (copia profunda)

"""

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista # copia

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que a atribução foi gerada tanto na lista nova quanto na antiga
# Isso é chamado em Python de Shallow Copy
