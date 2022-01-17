v1 = float(input('Digite a primeira medida: '))
v2 = float(input('Digite a segunda medida: '))
v3 = float(input('Digite a terceira medida: '))

if (v1 < (v2+v3)) and (v2 < (v1+v3)) and (v3 < v1+v2):
    if v1 == v2 and v1 == v3 and v2 == v3:
        print('Equilatero')
    elif v1 == v2 or v1 == v3 or v3 == v2:
        print('isoceles')
    else:
        print('Escaleno')
else:
    print('Nao é um triangulo!')