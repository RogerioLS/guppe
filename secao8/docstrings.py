"""
Documentando funções com Docstrings

Obs: Podemos ter acesso á documentação de uma função em python
utilizando o metodo especial __doc__

Podemos ainda fazer acesso á documentação com a funçaõ help()

"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quedrado de ''numero á potencia'' informada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por potencia
    """
    return numero ** potencia

