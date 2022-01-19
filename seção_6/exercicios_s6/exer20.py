lista = []
lista_par = []
cont = 0

while cont < 1000:
    cont += 1
    n = int(input('Digite um numero: '))
    if n == 1000:
        break
    else:
        lista.append(n)
        if n % 2 == 0:
            lista_par.append(n)
        else:
            continue

num_total = len(lista)
num_par = len(lista_par)

print(f'O total de numeros digitados foi {num_total}, e o total de numeros pares foi {num_par}.')