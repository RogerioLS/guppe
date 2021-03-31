"""
Dunder Nane e Dunder Main

Dunder -> Doble Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atribuitos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:
int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main(String[] args){
}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá á variavel __name__ o valor __main__ indicando que este módulo é o

Main -> Significa principal.
Name -> Proprio arquivo.

"""

from funcoes import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))
