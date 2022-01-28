matriz = []
maior_queDez = 0

for l in range(4):
    linha =[]
    for c in range(4):
        num = int(input('Digite um Número: '))
        if num > 10:
            maior_queDez += 1
        linha.append(num)
    matriz.append(linha)

print(f'A matriz acima possui {maior_queDez} valores maiores que Dez.')