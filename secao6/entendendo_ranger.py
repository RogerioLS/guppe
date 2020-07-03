"""
Ranges
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range pra trabalhar melhor com loops for.
Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria
mas sim de maneira especificada.

Formas gerais:
# Forma 1:
range(valor_de_parada)
OBS: valor_de_parada nao inclusive(inicio padrao 0, e passo de 1 em 1)
for num in range(11):
    print(num)

# Forma 2:
range(valor_de_inicio, valor_de_parada)
OBS: valor de parada não inclusive(inicio especificado pelo usuario, e passo em 1 em 1)
for num in range(4, 11):
    print(num)

# Forma 3:
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor de parada não inclusive(inicio especificado pelo usuario, e passo especificado pelo usuario)
for num in range(5, 55, 5):
    print(num)

# Forma 4:
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor de parada não inclusive(inicio especificado pelo usuario, e passo especificado pelo usuario)
for num in range(10, -1, -1):
    print(num)

"""