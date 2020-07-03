"""
Definindo funções

- Funções são pequenos trechos de codigo que realizam tarefas especificas
- Pode ou não receber estrada de dados e retornar uma saida de dado;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se voce escrever uma funçao que realizar varias tarefas ddentro dela;
é bom fazer um verificação para que a função seja simplificada.

já utilizamos varias funçoes desde que iniamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muito;
"""
# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']
# Utilizando a função integrada (Built-in) do Python print()
print(cores)

curso = 'Programação em Python: Essencial'
print(curso)

cores.append('roxo')
print(cores)

# curso.append('Mais dados...') # AttributeError
# print(curso)

cores.clear()
print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself -  não repita o codigo
# Mas então , como definir funções?

"""
Em Python, a forma geral de definir uma funçao é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde: 
nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underLine(Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não:
bloco_da_funcao -> Tembém chamado de corpo da função ou implementação, é onde o processamento da funçao acontece.
Neste bloco, pode ter ou não retorno da funçao.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao PyThon que estamos definindo
uma funçao. Tambem abrimos o bloco de codigo com o já conhecido dois ponto ':' que é 
utilizado em Python para definir blocos.
"""

# Definindo a primeira função
# Definição

def diz_oi():
    print('oi')

"""
OBS: 
1 - Veja que, dentro das nossas funções podemos utilizar outras funçoes;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela fas é dizer oi:
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando funções
# Chamada de execução
diz_oi() # nunca esquece de colocar os parentes, se não, não executa

# Exemplo 2
def cantar_parabens():
    print('Parabens pra voce')
    print("Nesta data querida")
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

for n in range(5):
    cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta funçao atraves da variavel

canta = cantar_parabens
canta()

