"""
Geradores

- Geradores (Generators) são Iterators (Iteradores)

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield:
- Generators podem ser criados com Expressões Geradoras:

Diferenças entre Funções e Generator Functions (Funções Geradoras)

--------------------------------------------------------------------------------------
| Funções                                  | Generator Functions                     |
--------------------------------------------------------------------------------------
- Utiliza return                           | - Utilizam yield                        |
- Retorna uma vez                          | - Podem utilizar yield múltiplas vezes  |
- Quando executada, retorna um valor       | - Quando executada, retorna um generator|
--------------------------------------------------------------------------------------
"""

# Exemplo Generator Function


def conta_ate(valor_maximo):
    """ Uma Generator Function não é um Generator. Ela gera um generator """
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
for num in gen:
    print(num)
