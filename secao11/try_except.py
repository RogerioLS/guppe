"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. previnido
assim que o programa para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema


# Exemplo 1 - Tratamento um erro generico

try:
    rogerio()
except:
    print('Deu algum problema')

# Tente executar a função rogerio(), caso você encontre erros, imprima a mensagem de erro.


# Exemplo 2

try:
    len(5)
except:
    print('Deu algum problema')


# Exemplo 3 - Tratando um erro específico

try:
    rogerio()
except NameError:
    print('Você está utilizando uma função inexistente')


# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Deu algum problema')


# Exemplo 5 - Tratamento um erro especifico com detalhe do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Exemplo 6 - Podemos efetuar diversos tratamentos de erros de uma vez

try:
    rogerio()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print(f'Deu um erro diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Rogerio"}

print(pega_valor(dic, 'nome'))




















