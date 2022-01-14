from math import log

num = int(input('Digite um numero: '))

if num < 0:
    print('Numero invalido!')
else:
    l = log(num)
    print(f'O logaritmo do numero informado acima é {l}')
