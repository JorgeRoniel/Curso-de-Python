lista_positivos = []
negativos = 0

for i in range(0, 10):
    num = int(input('Insira um numero: '))
    if num > 0:
        lista_positivos.append(num)
    else:
        negativos += 1

soma = sum(lista_positivos)

print(f'A soma dos numeros positivos é {soma},\nE a quantidade de numeros negativos é {negativos}')