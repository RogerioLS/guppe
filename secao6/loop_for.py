"""
Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java
for(int = 0; i < 10; i++){
    //execução
}

Utilizamos loops para iterar sobre sequência ou sobre valores iteraveis
Exemplos de iteraveis:
-   String
nome = 'Geek University'
-   Lista
lista = [1,3,5,7,9]
-   Range
numeros = range(1, 10)

#Exemplo for 1
for letra in nome:
    print(letra)

#Exemplo for 2
for numero in lista:
    print(numero)

#Exemplo for 1
#O valor final não é inclusive
for numero in range(1, 10):
    print(numero)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor) # [0] [1]

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')


nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

"""



for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
