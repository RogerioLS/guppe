"""
Decoradores (Decorators)

O que são decorators

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamento;
- Decorators também são exemplos de Higher Order Functions:
- Decorators tem uma sintaxe própria, usando "@" (Syntavt Sugar / Açucar Sintatico)


"""

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Bem-vindo ao curso de Python')


def raiva():
    print('SAI DAQUI!!!!!')

# Testando


teste = seja_educado(raiva)
teste()

print(' * ---------------- DECORATORS --------------------- * ')


def seja_educado_mesmo(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo


@seja_educado_mesmo
def apresentado():
    """ Decorators com Syntax Sugar (Açucar Sintático) """
    print('Meu nome é Rogério')

# Testando


apresentado()


@seja_educado_mesmo
def dormir():
    print('Quero dormir....')


dormir()
