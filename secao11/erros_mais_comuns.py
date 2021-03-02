"""
Erros mais comum em Python

É importante presta atenção e apreende a ler as saidas de erros geradas pela execuçã
do nosso codigo.

1 - SyntaxERROR ex:
a) def funcao:
    print('nome')

b) def = 1

c) return

2 - NameERROR -> ocorre quando uma variavel ou funçao não foi definida ex:

a) print(nome)

b) geek()

3 - TypeERROR -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado ex:

a) print(len(5))

b) print('nome' + [])

4 - IndexERROR -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo
de dado indexado utilizado um indice invalido, valido para list e tupla
a) lista = ['nome']
print(lista[2])

5 - ValueERROR -> Ocorre quando uma funcao/operacao/ buit-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado. ex:

a) print(int('nome'))

6 - KeyERROR -> Ocorre quando tentamos acessar um dicionario com uma chave que nao existe
ex:

a)dic = {'python': 'rogerio'}
print(dic('lopes'))

7 - AttributeERROR -> Ocorre quando uma variavel não tem um atributo/funcao ex:

a) tupla = {11, 2, 3, 7}
print(tupla.sort())

8 - IndentationERROR -> Ocorre quando não respeitamos a indentacao do python(4 espaco) ex:

a)
def nova():
print('nome')

b)
for i in range(10):
i+1

"""




