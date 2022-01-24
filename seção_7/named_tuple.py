"""
Modulo Collections: Named Tuple

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome para a mesma e
tambem parametros

"""

#Como Usar:

from collections import namedtuple

#Forma 1 - Declaração da Tuple
cachorro = namedtuple('cachorro', 'raça nome idade')

#Forma 2 - Declaração da Tuple
cachorro = namedtuple('cachorro', 'raça, nome, idade')

#Forma 3 - Declaração da Tuple
cachorro = namedtuple('cachorro', ['raça', 'nome', 'idade'])

#Usando

rex = cachorro(idade=1, raça='pitbull', nome='rex')

#Acessando os valores

#Forma 1
print(rex[0])
print(rex[1])
print(rex[2])

print('')

#Forma 2
print(rex.idade)
print(rex.raça)
print(rex.nome)