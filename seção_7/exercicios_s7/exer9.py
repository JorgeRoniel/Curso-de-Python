lista = []

j = 0
while j < 6:
    j += 1
    num = int(input('Insira um numero par: '))
    if num % 2 == 0:
        lista.append(num)
    else:
        continue

print(lista[::-1])