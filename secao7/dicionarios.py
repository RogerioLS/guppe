"""
Dicionsrios

OBS: em algumas linguagens são conhecidos como mapa

Dicionario são coleções do tipo chave/valor.

Dicionários são representados por chaves{}
print(type({}))

OBS: sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave qaunto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1 (Mais Comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)
print(type(paises))

# Forma 2 (Menos Comum)

paises = {br='Brasil', eua= 'Estados Unidos'}
print(paises)
print(type(paises))




# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos um erro
# Forma 2 - Acessando via get - Remomendada

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru')
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o país')

pais = paises.get('ru', 'Não encontrei')
print(f'Encontrei o país {pais}')






# Ele sempre busca pela chave e não pelo valor
# Verificação se existe a chave
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']




# Podemos utilizar qualquer tipo de dado(int, float, string, boolean), inclusive lista, tupla dicionario, como chaves
# de dicionarios.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesma
# são imutaveis

localidades = {
    (35.342, 36.654): 'Escritorio em Tókio',
    (54.654, 32.453): 'Escritorio em Nova York',
    (30.231, 45.654): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1
receita['abr'] = 400
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)





# Atualizando dados em um dicionário
# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novo elementos ou atualizar dados em um dicionario é a mesma.
# CONCLUSÃO 2: Em dicionarios, NÂO podem ter chaves repetidas.




# Remover dados de um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1
ret =  receita.pop('mar')
print(ret)
print(receita)

# OBS: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)
del receita['fev']
# Não se remove a chave duas vezes
"""

# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
        
        # 1 - poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Play Systation', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ('Play Systation', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)

# Teriamos que saber qual é o indice de cada informação no produto

# 3 - Poderiamos utilizar um Dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 130.00}

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.




d = dict {'a': 1, 'b': 2, 'c': 3}
print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)
d.clear()
print(d)

# Copiando um dicionario para outro
# Forma 1
novo = d.copy() # Deep Copy
print(novo)

novo['d'] = 4
 print(d)
 print(novo)

# Forma 2 # Shallow Copy

novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)
"""

# Forma não usual de criaçao de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'e-mail', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parametros: um interavel e um valor
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a está chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)