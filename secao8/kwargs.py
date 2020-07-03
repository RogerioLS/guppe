"""
**kwargs

Este é só mais um parâmetro , mas diferente do *args que coloca os valores extras
em uma tupla, o **kargs exige que utilizemos parametros nomeados, e transforma esses
parâmetros extras em um dicionário.



# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(rogerio='preto')

# OBS: os parametos *args e **kwargs não são obrigatorios
cores_favoritas()



# exemplo mais complexo

def cumprimento_especial(**kwars):
    if 'geek' in kwars and kwars['geek'] == 'python':
        return 'Você recebeu um cumprimento Pytonico Geek'
    elif 'geek' in kwars:
        return f"{kwars['geek']} Geek!"
    return 'Não tenho certeza quem você é .....'

print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))



# Nas nossas funções, podemos ter (NESTA ORDEM)
- Parametros obrigatorios
- *args:
- Parametros default(não obrigatorio):
- **kwargs
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Rogerio', 2,3,4, solteiro=True)
minha_funcao(26, 'Ana', eu='Nao', voce='Vai')
minha_funcao(19, 'Carla', 2,4,5, java='True', python='True')



# entenda por é importanten a ordem dos parametros

# funcao com ordem correta dos parametros
def mostra_info(a, b, *args, instrutor='geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

# funcao com ordem incorreta dos parametros
def mostra_info(a, b, instrutor='geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1,3,4,sobrenome='University', cargo='Instrutor'))



# desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Rogerio', 'sobrenome': 'Lopes'}
print(mostra_nomes(**nomes))

"""

def soma_multiplos_numeros(a,b,c):
    print(a+b+c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)
# OBS no kwargs temos que informar o mesmo parametros da funçao 































