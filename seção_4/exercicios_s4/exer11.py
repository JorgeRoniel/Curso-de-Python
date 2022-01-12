from math import sqrt


a = int(input('Digite a medida do primeiro cateto: '))
b = int(input('Digite a medida do segundo cateto: '))

h = sqrt((a**2)+(b**2))

print(f'A medida da hipotenusa é {h}')