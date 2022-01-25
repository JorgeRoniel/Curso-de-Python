lista = []

for i in range(0, 5):
    num = int(input('Digite um numero: '))
    lista.append(num)

maior = max(lista)
menor = min(lista)
media = sum(lista) / 5

print(f'O maior numero informado foi {maior}')
print(f'O menor numero informado foi {menor}')
print(f'A media dos numeros informados é {media}')