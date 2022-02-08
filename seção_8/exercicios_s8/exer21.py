def primos_abaixo(num):
    primos = []
    for c in range(2, num):
        cont = 0
        for x in range(2, c):
            if (c % x) == 0:
                cont += 1
        
        if cont == 0:
            if c < num:
                primos.append(c)
    
    return f'A quantidade de numeros primos abaixo de {num} é {len(primos)}'

num = int(input('Entre com um numero: '))

res = primos_abaixo(num)
print(res)