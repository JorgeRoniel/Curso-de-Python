lista = []

j = 0
while j < 50:
    j += 1
    valor = (j + 5 * j) % (j + 1)
    lista.append(valor)

print(lista)
