from math import sqrt

num = float(input('Digite um numero: '))

if num > 0:
    r = sqrt(num)
    q = num ** 2
    print(f'A raiz quadrado do numero digitado é {r}\nE o quadrado dele e {q}')
else:
    print('valor invalido!')
