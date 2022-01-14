h = float(input('Informe sua altura: '))
sexo = input('Informe seu sexo, Masculino(M), Feminino(F): ')

if sexo == 'M':
    peso = (72.7*h) - 58
    print(f'Seu peso ideal é {peso}')
elif sexo == 'F':
    peso = (62.1*h) - 44.7
    print(f'O seu peso ideal é {peso}')
else:
    print('Ocorreu algo de errado, tente novamente!')