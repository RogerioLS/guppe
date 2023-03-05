"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime
"""

import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minite, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajuste da data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Acessa individual dos elementos de data hora
evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

# Input data
nascimento = input('Informa sua data de nasciento (dd/mm/yyyy)')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
