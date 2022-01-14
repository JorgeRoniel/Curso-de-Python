"""
Estruturas Condicionais
if, else, elif

if condição:
    algo para acontecer
elif outra condição:
    outra coisa para acontecer
else:
    se nada der certo, essa é a ultima coisa para acontecer

Estruturas logicas
and, or, not, is

"""

idade = int(input('Digite sua idade: '))

if idade >= 18 and idade < 60:
    print('Voce e maior de idade.')
elif idade < 18:
    print('Voce e menor de idade.')
else:
    print('se voce tiver mais de 60, voce e idoso.')