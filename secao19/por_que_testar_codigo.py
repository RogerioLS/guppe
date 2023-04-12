"""
Por que testar nosso código?

Teste Automatizados!

--------------
Por que testar nosso código?
    - Reduzir bugs (problemas) no código existe:
    - Testes garantem que novos recursos da sua aplicação não quebram (alterem) recurso antigos:
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos:
    - Testes garatem que a refatoração que costuamos e fazer não tragam novos bugs (problemas):

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primario:
    - Então você escreve o código minimo suficiente para fazer o teste passar (ou seja, executar com sucesso):
    - Então refatora o código para realizar a funcionalidade e testar novamente:
    - Uma vez que o teste passa, recurso é considerado completo:

Estes estágios de desenvolvimento do TDD são quase um mantra que as desenvolvidores seguem, conhecido como:
    - Red;
    - Green;
    - Refactor;
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
