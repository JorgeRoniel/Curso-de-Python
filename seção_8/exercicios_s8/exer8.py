from math import sqrt

def pitagoras(a, b):
    h = sqrt(((a**2) + (b**2)))

    return h

cat_a = int(input('Digite o valor do primeiro cateto: '))
cat_b = int(input('Digite o valor do segundo cateto: '))

result = pitagoras(cat_a, cat_b)

print(f'O valor da hipotenusa desse triangulo é {result}')