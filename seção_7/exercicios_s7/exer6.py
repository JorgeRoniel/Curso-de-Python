lista = []

for c in range(0, 10):
    num = int(input('Insira um numero: '))
    lista.append(num)

maior = max(lista)
menor = min(lista)

print(f'O maior valor informado foi {maior}, e o menor valor informado foi {menor}')