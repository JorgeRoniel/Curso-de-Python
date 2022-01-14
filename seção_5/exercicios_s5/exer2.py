from math import sqrt

num = int(input('Digite um numero: '))

if num > 0:
    raiz = sqrt(num)
    print(f'A raiz quadrada do numero digitado e {raiz}')
elif num <= 0:
    print('Valor invalido!')
