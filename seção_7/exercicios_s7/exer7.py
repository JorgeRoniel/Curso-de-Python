lista = []

for c in range(0, 10):
    num = int(input('Insira um numero: '))
    lista.append(num)

maior = max(lista)
posicao = lista.index(maior)

print(lista)
print(f'{maior} é o maior valor da lista.')
print(f'Sua posição na lista é {posicao}')
