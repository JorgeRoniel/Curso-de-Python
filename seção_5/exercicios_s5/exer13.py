nota1 = float(input('Digite sua nota do trabalho de laboratorio: ')) #peso 2
nota2 = float(input('Digite sua nota da avaliaçao semestral: ')) #peso 3
nota3 = float(input('Digite sua nota do exame final: ')) #peso 5

if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10):
    print('Valores invalidos!')
else:
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

    if media == 0 or media <= 2.9:
        print(f'Sua media é {media}, voce foi reprovado.')
    elif media == 3 or media <= 4.9:
        print(f'Sua media é {media}, voce esta de recuperaçao.')
    else:
        print(f'Sua media é {media}, voce esta aprovado.')