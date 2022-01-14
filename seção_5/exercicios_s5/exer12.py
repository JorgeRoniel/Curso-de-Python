peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif imc >= 18.6 or imc <=24.9:
    print('Voce esta saudavel!')
elif imc >= 25 or imc <=29.9:
    print('Voce esta com peso em excesso!')
elif imc >= 30 or imc <= 34.9:
    print('Voce esta com obesidade grau 1!')
elif imc >= 35 or imc <= 39.9:
    print('Voce esta com obesidade grau 2!')
elif imc >= 40:
    print('Voce esta com obesidade grau 3! cuidado!!')
else:
    print('Ocorreu algo errado, tente novamente!')
