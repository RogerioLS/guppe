"""
Criando sua propria versão de loop

"""

for num in [1, 2, 3, 4, 5]:
    print(num)

# Fazendo na mão


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Rogerio Lopes')
