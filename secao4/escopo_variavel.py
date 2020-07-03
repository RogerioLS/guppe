"""
Escopo de variaveis, temos dois casos de escopo:
1 -> Variaveis Globais, são reconhecida em todo o programa
2 -> Variaveis Locais, são reconhecida só em um suposto escopo declarado

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variavel, nos não colocamos o tipo de dado dela
isto é feito por exemplo em linguagens como JAVA , C Ex:

int numero = 42;
"""

numero = 42 #Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existe = 'oi'
print(nao_existe)

numero = 42
#novo = 0
if numero > 10:
    novo = numero + 10 #exemplo de variavel local
    print(novo)
print(novo)
