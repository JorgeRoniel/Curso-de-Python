nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = ((nota1*1) + (nota2*1) + (nota3*2)) / 4

if media >= 60:
    print(f'Sua media é {media}, voce esta aprovado!')
elif media < 60:
    print(f'Sua media é {media}, voce foi reprovado.')
else:
    print('Algo deu errado, tente novamente!')