"""
Try / Except / Else / Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA!

# Else -> é executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voceê digitou {num}')

# Finally
# OBS: bloco Finally é SEMPRE executado. Independete se houve exceção ou não
# É utilizado para fechar ou desalocar recursos.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor não digitou um valor válido')
else:
    print(f'Voceê digitou o numero {num}')
finally:
    print('Executando o finally')


def dividir(a, b):
    return a / b


try:
    num1 = int(input('Informe o primeiro número: '))
except ValueError:
    print('O valor precisa ser numerio')
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numerio')
try:
    print(f'O resultado da divisão foi de: {dividir(num1, num2)}')
except NameError:
    print('Valor incorreto')


# Maneira mais limpa Generico
def dividir(a, b):
    try:
        return f'O resultado da divisão foi de: {int(a) / int(b)}'
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))
"""

# Maneira mais limpa Semi-Generico


def dividir(a, b):
    try:
        return f'O resultado da divisão foi de: {int(a) / int(b)}'
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(dividir(num1, num2))

