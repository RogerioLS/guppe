"""
Decorators com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto chamado Decorator Patterr

# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
"""

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhamento de {acompanhamento}, por favor.'

# Testando


print(saudacao('Rogerio'))
# print(ordenar('Picanha', 'Batata Frita'))  # Vai gerar um erro pois só passamos um parametro no UPPER

""" Refatorando com o uso Decorator Patterr """


def gritar_(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar_
def saudacao_(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar_
def ordenar_(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhamento de {acompanhamento}, por favor.'

# Testando


print(saudacao_('Rogerio'))
print(ordenar_('Picanha', 'Batata Frita'))
print(ordenar_(acompanhamento='Batata Frita', principal='Picanha'))

""" Decorator com argumento """


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando


print(soma_dez(10, 12))
print(soma_dez(1, 12))  # Valor incorreto! Primeiro argumento precisa ser 10

print(comida_favorita('pizza', 'lanche'))
print(comida_favorita('lanche', 'pizza'))  # Valor incorreto! Primeiro argumento precisa ser pizza
