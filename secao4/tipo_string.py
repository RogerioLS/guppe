"""
Tipo String, Em python um dado é considerado do tipo string sempre que:
- Estiver entre áspas simples -> 'uma string', '234', 'True'
- Estiver entre áspas duplas -> "uma string", "234", "True"
- Estiver entre áspas simples triplas-> '''uma string''', '''234''', '''True'''

nome = 'Geek university'  ou COM "", ''' ''', """ """
print(nome)
print(type(nome))

para pular linha acrescente /n

nome = 'Angelina /nJolie'

print(nome.upper) transforma tudo em maiusculo
print(nome.lower) transforma tudo em minusculo
print(nome.split) transforma em lista de string
print(nome[0:4])  Slice de string 
print(nome[5:15]) Slice de string

[   0  ,       1  ]
['Geek', 'University']
print(nome.split()[0])
print(nome.split()[1])
"""
#Estiver entre áspas simples -> """uma string""", """234""", """True"""

nome = 'Geek University'
print(nome[::-1]) # -> comece do primeiro elemento e inverta
print(nome.replace('G','R'))

texto = 'socorram me subino onibus em marrocos'
print(texto) #mais conhecido como palindrumo 
print(texto[::-1])