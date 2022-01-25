lista_par = []
lista_total = []

for c in range(0, 10):
    num = int(input('Insira um numero: '))
    lista_total.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    
total_par = len(lista_par)
print(f'O total de numeros pares digitados foi {total_par}')
print(lista_total)
