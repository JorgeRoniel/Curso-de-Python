lista = []

for n in range(0, 10):
    num = int(input('Digite um numero: '))
    lista.append(num)
    soma = sum(lista)
    

print(f'A soma dos valores é {soma}')