from math import sqrt

def quadrado_perfeito(num):
    if num > 0:
        raizq = int(sqrt(num))
        if (raizq ** 2) == num:
            print('esse numero é um quadrado perfeito.')
        else:
            print('esse numero não é um quadrado perfeito.')
    else:
        print('um quadrado perfeito deve ser positivo, tente novamente.')


quadrado_perfeito(17)