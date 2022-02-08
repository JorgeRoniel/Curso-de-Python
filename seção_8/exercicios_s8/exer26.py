def somatorio(num):
    lista = []
    for x in range(1, num + 1):
        lista.append(x)

    soma = sum(lista)

    return f'O somatorio de 1 até {num}, é {soma}'

n = int(input('Entre com um numero: '))
res = somatorio(n)

print(res)