nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if (nota1 > 10 or nota1 < 0) or (nota2 > 10 or nota2 < 0):
    print('As notas não são validas!')
else:
    media = (nota1 + nota2)/2
    print(f'As notas são validas, e a sua media é {media}')
