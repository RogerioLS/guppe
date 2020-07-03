"""
Funcoes com retorno

numeros = [1,2,3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'retorno de print: {ret_pr}')

Obs: Em python, quando uma função não retorna nenhum valor, o retorno é none
     Funções Python que retornam valores, devem retornar estes valores com a
     palavra reservada return.
     Não precisamos necessariamente criar uma variavel para receber o retorno
     de uma função.Podemos passar a execução da função para outras funções.


# Vamos refatorar esta função para que ela retorno o valor
def quadrado_de_7():
    return 7 * 7

# Criamos uma varíavel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno : {ret}') #ou
print(f'Retorno : {quadrado_de_7() + 1}')


# Refatorando a primeira função
def diz_oi():
    return 'oi'
print(diz_oi())
alguem = 'Rogério!'
print(diz_oi() + alguem)

Obs: Sobre a palavra reservada return
1 - Ela finalza a função, ou seja, ela sai da execução da função:
2 - Podemos ter, em uma função, diferentes, returns:
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores:


# Exemplo 1

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi!'
    print('Estou sendo executado apos o retorno')

print(diz_oi())




# Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3
def outra_funcao():
    return 2,3,4,5

num1 , num2, num3, num4 = outra_funcao()
print(num1,num2,num3,num4)

print(outra_funcao())
print(type(outra_funcao()))


# Vamos criar uma função para jogar moeda

from random import random

def jogar_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    # valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(jogar_moeda())

"""

# Erros comuns na utilização de retorno, que na verdade nem é erro, mas sim codificação desnecessaria.

print('Digite o numero')
numero = float(input())
def eh_impar_uo_par():
    if numero %2 != 0:
        return 'Par'
    return 'Impar'

print(f'O numero digitado é: {eh_impar_uo_par()}')




























