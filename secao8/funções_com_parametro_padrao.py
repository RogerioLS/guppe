"""
Funçoes com Parametros padrao

- Funçoes onde a passagem de parametro seja opcional;

# Exemplo de função opicional
print('Rogerio')
print()

# Exemplo de função onde a passagem de parametro seja obrigatoria
def quadrado(numero):
    return numero **2

print(quadrado(9))
print(quadrado())


# Exemplo # Lembrando que se você chamar a função sem colocar nenhum parametro ela por default vai
#  # excutar o que estava declarado na funcao
def exponencial(numero=4, potencia=5):
    return numero ** potencia

print(exponencial(3,4))
print(exponencial())
print(exponencial(3))


# Exemplo
# Obs em funçaõ python os parametros com valores default (padrao) devem sempre estar
# ao final da declaração
# ERRO
def teste(potencial, num=2)
    return num ** potencial


# Exemplo mais complexo
def mostra_informacao(nome='Rogerio', instrutor=False):
    if nome == 'Rogerio' and instrutor:
        return 'Bem vindo instrutor Rogerio'
    elif nome == 'Rogerio':
        return 'Eu pensei que você fosse um instrutor'
    return f'Ola {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Rodrigo'))

# Quais tipos de valores podemos utilizar como  default para parametros
# numeros, string, floats, boolean, lista, tuplas, dicionarios, funçoes e etc


# Exemplo

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtração(num1, num2):
    return num1 - num2

print(mat(2,3))
print(mat(2, 2, subtração))


# Escopo -  Evitar problemas e confusões
# Variaveis globais
# Variaveis Locais

instrutor = 'Rogerio' # variavel global é ignorada quando se ha uma mesma variavel com nome igual no def

def diz_oi():
    instrutor = 'Rodrigo' # Variavel local
    return f'oi {instrutor}'

    def diz_oi():
    prof = 'Rodrigo'
    return f'oi {prof}'

print(diz_oi())
print(prof) # nameError


# Atenção com variaveis globais (se puder evitar, evite)
total = 0

def incrementa():
    total = total +1
    return total

print(incrementa())


# Avisando o def para utilizar a variavel global
total = 0

def incrementa():
    global total
    total = total +1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funçoes que sao declaradas dentro de funções e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 1

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro


print()
print()
print()































