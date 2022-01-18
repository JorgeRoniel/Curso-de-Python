lista = []

for n in range(0, 10):
    num = int(input('Insira um numero: '))
    if num  < 0:
        continue
    else:
        lista.append(num)
        media = sum(lista)/10

print(f'A media dos valores é {media}')