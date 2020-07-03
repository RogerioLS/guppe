"""
Loop While, forma geral
while expressao_booleana: // execuçao do loop
O bloco do while será repetido enquanto a expressão booleana for verdadeira,
Expressão Booleana é toda expressao onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5
num < 5

Exemplo 1
numero = 1
while numero < 10:
    print(numero)
    #numero = numero + 1
# OBS: em um loop while é importante que cuidemos do critério de parada para
# não causar um loop infinito


"""

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')