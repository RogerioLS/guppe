"""
Teste de Velocidade com Expressões Geradoras


"""

# Realizando o teste de velocidade
import time

# Generator Expression - Executou em 3 segundos mais rápido que List
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
