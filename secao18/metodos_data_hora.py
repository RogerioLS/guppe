"""
Métodos de Data e Hora
"""

import datetime
import timeit
from textblob import TextBlob
import functools

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorendo á meia-noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana. weekday()
print(manutencao.weekday())

aniversario = '08/11/1991'  # input('Qual sua data de nascimento? dd/mm/yyyy:  ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em uma sábado-feira')
elif aniversario.weekday() == 6:
    print('Você nasceu em uma domingo-feira')

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto


def formata_data_if(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


def formata_data(data):
    return f'{data.day} de {TextBlob(data.strftime("%B"))} de {data.year}'


hoje = datetime.datetime.today()
print(formata_data(hoje))
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)

# Somente a hora
almoco = datetime.time(12, 30, 0)
print(almoco)

# Marcando tempo de execução do nosso código com timeit
# Loop for
tempo = timeit.timeit('".".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comphension
tempo = timeit.timeit('".".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('".".join(map(str, range(100)))', number=10000)
print(tempo)


def num(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(num, 2), number=10000))
