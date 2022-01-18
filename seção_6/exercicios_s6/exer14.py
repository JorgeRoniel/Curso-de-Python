num = int(input('Digite um numero par: '))

if num % 2 == 0:
    lista_par = []
    for c in range(0, num):
        if c % 2 == 0:
            lista_par.append(c)
        else:
            continue
    print(lista_par[::-1])
else:
    print('Esse valor não é par, tente novamente!')