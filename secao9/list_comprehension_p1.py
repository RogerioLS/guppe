"""

List Comprehesion

- Utilizado list comprehesion nos podemos gerar novas listas com dados
processados a partir de outro iteravel.

# Sintaxe da list Comprehesion
[dado for dado in iteravel]



# Exemplos
# para cada numero que estiver na lista de numeros multiplique por 10
# e me retorne uma nova lista, po ser / + ou - tambem
numeros = [1,2,3,4,5]

res = [numero * 10 for numero in numeros]
print(res)

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor*valor


res = [funcao(numero) for numero in numeros]
print(res)



# List Comprehesion versos Loop

numeros = [1,2,3,4,5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehesion
print([numero * 2 for numero in numeros])

"""

# outro exemplos

nome = 'Rogerio Lopes'
print([letra.upper() for letra in nome])

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['rodrigo', 'joao', 'rogerio']
print([caixa_alta(amigo) for amigo in amigos])

#3
print([numero * 3 for numero in range(1,10)])

#4
print([bool(valor) for valor in [0, [], '', True, 3.14]])

#5
print([str(numero) for numero in [1, 2, 3, 4, 5]])









