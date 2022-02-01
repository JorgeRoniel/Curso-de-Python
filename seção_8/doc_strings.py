"""
Documentando funções com Docstrings

OBS:
- Podemos ver a documentação de uma função usando o metodo especial '__doc__'.
"""

#Exemplo:

def diga_oi():
    """Uma simple função que mostra na tela um 'Oi'"""
    return 'Oi'

#Exemplo OBS_1:
print(diga_oi.__doc__)

def media(n1, n2, n3):
    """
    Essa função recebe três parametros e mostra a media dos valores informados.
    
    :Param1 n1: Recebe o primeiro valor;
    :Param2 n2: Recebe o segundo valor;
    :Param2 n2: Recebe o terceiro valor;
    :return: Retorna a soma dos três valores e a divisão pelo resultado da soma (média).
    """
    return (n1 + n2 + n3) / 3