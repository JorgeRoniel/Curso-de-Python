matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for l in range(0, 5):
    for c in range(0, 5):
        if matriz[l] == matriz[c]:
            matriz[l][c] = 1

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]}]', end='')
    print()
