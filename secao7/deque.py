"""
Modulo Collections - Deque

podemos dizer que o deque é uma lista de alta performance
"""

# importe
from collections import deque

# criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # adiciona no final
print(deq)

deq.appendleft('k') # adicionar no começo
print(deq)

# Remover elementos
print(deq.pop()) # remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # remove e retorna o primeiro elemento
print(deq)