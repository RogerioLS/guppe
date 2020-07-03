"""
Tipo None

O tipo de dado None em python representa o tipo sem tipo, ou poderia ser conhecido também
como tipo vazio, porém, falar que é um tipo sem tipo é mais apropriado.

OBS: O tipo None é sempre especificado com a primeira letra maiúscula.

Certo: None
Errado: none

- Podemos utilizar None quando queremos criar uma variavel e inicializa-la com um tipo sem tipo, antes
de recebemos um valor final.

OBS: O tipo None em python é sempre considerado como False

"""

numeros = None
print(numeros)
print(type(numeros))

numeros = 1.44, 1.55, 1.66
print(numeros)
print(type(numeros))


n = int(input("N:"))
def asterisco(n):
    if n>0:
        asterisco(n-1)
        print('\U0001F60D')

        for i in range(n):
            print('\U0001F60D')
        asterisco(n-1)
    return n

print(asterisco(n))

