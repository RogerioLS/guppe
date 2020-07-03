"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python são representados por chave {}

print(receita)

# Interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')








print(receita.keys())

# esse é modelo pytonico de ser
for chave in receita.keys():
    print(receita[chave])




print(receita.values())
for valor in receita.values():
    print(valor)




# Desempacotamento de dicionarios
print(receita.items())
for chave, valor in receita.items():
    print(f'chave={chave} e valor = {valor}')










"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}

# Soma, valor maximo, valor minimo, tamanho
# Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))