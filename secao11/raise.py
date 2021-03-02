"""
Levantando os próprios erros com raise

raise -> não é uma função é uma palavra reservada que serve para criar as
nossas proprias exceções e mensagens de erro.

OBS: Nada depois do RAISE é executado.
"""

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise TypeError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('True', 'preto')
