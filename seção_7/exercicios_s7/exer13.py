lista = []

for i in range(0, 5):
    num = int(input('Digite um numero: '))
    lista.append(num)

maior = max(lista)
menor = min(lista)
posicao_maior = lista.index(maior)
posicao_menor = lista.index(menor)

print(f'A posição do maior valor é {posicao_maior}, e a posição do menor é {posicao_menor}')