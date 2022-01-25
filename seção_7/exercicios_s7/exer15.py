lista = []

for x in range(0, 20):
    num = int(input('Digite um numero: '))
    lista.append(num)

lista_sem_rep = set(lista)

print(lista_sem_rep)