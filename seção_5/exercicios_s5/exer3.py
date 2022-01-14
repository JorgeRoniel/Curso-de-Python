from math import sqrt

num = float(input('Digite um numero real(quebrado): '))

if num > 0:
    raiz = sqrt(num)
    print(f'A raiz quadrada de {num} e {raiz}')
elif num < 0:
    quadrado = num ** 2
    print(f'O quadrado de {num} é {quadrado}')
else:
    print('Valor invalido!')