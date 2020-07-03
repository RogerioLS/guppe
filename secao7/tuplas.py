"""
Tuplas (tuple)
Tuplas são basicamente duas diferenças básicas:

1- As tuplas são representadas por parenteses()
2- As tuplas são imutáveis: isso siginifica que ao se criar uma tupla a
operação em uma tupla gera uma nova tupla

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # isso não é tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# Tuplas são definidas pela vírgulas e requer parenteses


# podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))



# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)
# Lembrando que devem ter a mesma quantidade



# Soma, Valor max, Valor min e Tamanho se valores inteiros e reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))



# Concatenação de Tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # podemos sobrescrever
print(tupla1)




# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)



# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)




# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tupla('Geek University')
print(escola)
print(escola.count('e'))






# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em um coleção
# Exemplo1

meses = ('Janeiro', 'Fevereiro', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Iterar com While
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento está na tupla
print(meses.index('Janeiro')) # Caso não exista da Erro

# Slicing
# Tupla[inicio:fim:passo]
print(meses[5:9])




# - Porque usar tuplas ao inves de listas

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro.
# - Isso porque trabalhar com elementos imutaveis traz a segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4,5,6)

nova = nova + outra

print(nova)
print(tupla)



"""




