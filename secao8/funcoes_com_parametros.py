"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro das mesma;
Se a gente pensar em um programa qualquer, geralmente temos;
entrada -> processamento -> saida

Se a gente pensar em uma funcao, ja sabemos que temos funçoes que:
- nao possuem entrada;
- nao possuem saida;
- possuem entrada mas não possoem saida;
- nao possuem entrada mas possuem saida;
- possuem entrada e saida;


# Refatorando uma funcao

def quadrado(numero):
    #return numero*numero
    return numero ** 3

print(quadrado(7))
print(quadrado(2))

ret = quadrado(8)
print(ret)


# Funções pode ter n parametros de entrada. Ou seja podemos receber como entrada
# em uma função quantos parametros forem necessarios. Eles são separados por virgula.

# Exemplos

def soma(a, b):
    return a + b

def multiplicação(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 3))
print(multiplicação(3,4))
print(outra(3, 9, 'Rogerio'))

# Obs se a gente informar um numero errado de parametro ou argumentos, teremos TypeError



# nomeando parametros

def nome_completo(nome, sobre_nome):
    return f'Seu nome completo é {nome} {sobre_nome}'

print(nome_completo('Rogerio', 'Lopes'))

# A diferença entre parametros e argumentos
# parâmetros são variaveis declaradas na definição de uma função:
# argumento são dados passados durante a execução de uma função:

# A ordem dos parametros importa!

nome = 'Rodrigo'
sobrenome = 'Sousa'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (KeyWord  Arguments
# Caso utilizamos nomes dos parametros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome =  'Rogerio', sobre_nome = 'Lopes'))
print(nome_completo(nome = nome, sobre_nome = sobrenome))
print(nome_completo(sobre_nome = 'Rodrigo', nome = 'Sousa'))
"""

# Erro comum na utilização de return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total+num
    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(soma_impares(lista))






















