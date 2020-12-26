"""
Estrutura lógicas: and(e), or(ou), not(não), is(é)
Operadores unários:
    - not
Operadores binarios:
    - and, or, is
"""

ativo = True
logado = True

"""if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
"""
#Se não estiver ativo
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usúario')

#ativo é verdadeiro?

print(ativo is True)
