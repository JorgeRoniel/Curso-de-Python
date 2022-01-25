lista = []

for x in range(0, 10):
    num = int(input('Digite um numero: '))
    lista.append(num)

lista_sem_rep = set(lista)
lista_com_rep = []

for c in lista_sem_rep:
    if lista.count(c) > 1:
        lista_com_rep.append(c)


print(f'Os valores repetidos foram:\n{lista_com_rep}')
