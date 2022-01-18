num = int(input('Digite um numero impar: '))

if num % 2 == 1:
    lista_impar = []
    for c in range(0, num):
        if c % 2 == 1:
            lista_impar.append(c)
        else:
            continue
    print(lista_impar)
else:
    print('Esse valor não é impar, tente novamente!')