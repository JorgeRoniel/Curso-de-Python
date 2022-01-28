lista1 = []
lista2 = []


for x in range(0, 5):
    n1 = int(input('Digite um numero: '))
    lista1.append(n1)

for i in range(0, 5):
    n2 = int(input('Digite um numero: '))
    lista2.append(n2)

lista3 = lista1 + lista2

lista3[::2] = lista1
lista3[1::2] = lista2

print(lista3)

    