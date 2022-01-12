total = 780_000

g1 = (total  * 46) / 100
g2 = (total * 32) / 100
g3 = total - (g1+g2)

print(f'O primeiro ganhador recebeu {g1}')
print(f'O segundo ganhador recebeu {g2}')
print(f'O terceiro ganhador recebeu {g3}')