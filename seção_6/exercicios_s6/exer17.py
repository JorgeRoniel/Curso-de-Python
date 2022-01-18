num = int(input('Insira um numero: '))

lista = []
for c in range(0, num + 1):
    lista.append(c)
    soma = sum(lista)

print(f'a soma dos primeiros {num} algarismos é {soma}.')