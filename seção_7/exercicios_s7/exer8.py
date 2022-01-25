lista = []

j = 0
while j < 6:
    j += 1
    num = int(input('Insira um numero: '))
    lista.append(num)

print(lista[::-1])