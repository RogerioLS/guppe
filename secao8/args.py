"""
Entendo o *args

- O *args é um parametro como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que começe com arterisco.

Exemplo:
*xis

Mas por convencção, utilizamos *args para defini-lo

Mas o que é o *args?
O parametro *args utilizado em uma função coloca os valores extras informados como
entrada em uma tupla. Então desde, já lembre-se que tuplas são imutaveis.

#Exemplo1

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(2,3,4))
print(soma_todos_numeros(2,4))
print(soma_todos_numeros(1,2,3,4))


# Entendendo o args

def soma_todos_numeros(nome, email,*args):
    return sum(args)

print(soma_todos_numeros('rogerio', 'joao',1,2,3,4,5,6,7))



# outro exemplo de utilizaçao de args

def verifica_info(*args):
    if 'Rogerio' in args and 'Lopes' in args:
        return 'Bem vindo Rogerio Lopes'
    return 'Você não o Rogério'

print(verifica_info())
print(verifica_info(1, True, 'Rogerio', 3, 'Lopes'))
print(verifica_info(False, 10, 'Lopes'))
"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

numeros = [1,2,3,4,5,6,7,8]

# Desempacotamento
print(soma_todos_numeros(*numeros))

# o asteristico serve para que informemos ao python que estamos
# passando como argumentos uma coleção de dados.

























