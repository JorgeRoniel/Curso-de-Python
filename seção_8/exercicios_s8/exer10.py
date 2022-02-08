def maior_menor(n1, n2):
    n1 > n2
    if n1 < n2:
        print(f'{n2} é maior que {n1}')
    else:
        print(f'{n1} é maior que {n2}')

n1 = int(input('Entre com um numero: '))
n2 = int(input('Digite outro numero: '))

maior_menor(n1, n2)