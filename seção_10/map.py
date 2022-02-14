"""
Função Map

- com o map, mapeamento de valores para funções.
- O map recebe dois parametros: uma função, um iteravel.
- Após a primeira utilização do map(), depois da utilização do resultado, ele zera.
"""

import math

def area(r):
    """Calcula a area de um circulo"""

    return math.pi * (r ** 2)

print(area(3))

#Utilizando o map():

raios = [2, 3, 7, 4, 10]

areas = map(area, raios)
print(list(areas))

#Map com lambda:

print(list(map(lambda r: math.pi * (r ** 2), raios)))