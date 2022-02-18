"""
Modulos Built_in (integrados)

- Podemos importar todas as funções de um modulo utilizando o '*'
EX:
    from random import *

- quadno formos utilizar a importação de varias funções de um mesmo modulo, colocamos em uma tupla
EX:
    from random import (
     choices,
     random,
     ranint
     )


"""

#Utilizando alias(Apelidos) para as importações.
from random import random as rzin

print(rzin())