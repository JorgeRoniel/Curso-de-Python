"""
matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um numero: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
"""

matriz = [] 
for i in range(0, 4):
    linha = [] 
    for j in range(0, 4):
        linha.append(int(input('Digite um numero: ')))
    matriz.append(linha)
    
for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz[i][j]}]', end='')
    print()

