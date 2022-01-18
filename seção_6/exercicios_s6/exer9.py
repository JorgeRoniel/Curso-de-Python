qtd = int(input('Digite a quantidade desejada de vezes que o loop vai acontecer: '))

lista_impar = []

for c in range(1, qtd):
    num = int(input('Insira um numero: '))
    if num % 2 == 1:
        lista_impar.append(num)
    else:
        continue

print(lista_impar)