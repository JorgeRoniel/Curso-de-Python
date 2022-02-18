"""
Pacotes em Python

- modulo é apenas um arquivo python que pode ter diversas funções para utilizarmos.
- pacote é um diretorio que armazena diversos modulos.

"""

from pac import mod1 as md1
from pac import mod2 as md2
from pac.pac2 import mod3 as md3
from pac.pac2 import mod4 as md4

print(md1.pi)
print(md1.funcao1(2, 10))
print(md2.funcao2())
print(md3.funcao3())
print(md4.funcao4())