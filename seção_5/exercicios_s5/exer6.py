num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    diferenca = num1 - num2
    print(f'O numero {num1} e maior que {num2}, e a diferença entre eles é {diferenca}')
elif num1 < num2:
    diferenca = num2 - num1
    print(f'O numero {num2} e maior que {num1}, e a diferença entre eles é {diferenca}')
else:
    print('Ambos sao iguais')

