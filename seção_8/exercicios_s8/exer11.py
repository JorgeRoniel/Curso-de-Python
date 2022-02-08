def medias(n1, n2, n3, *args):
    if 'A' in args:
        med = (n1 + n2 + n3) / 3
    elif 'P' in args:
        med = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    else:
        return 'Error, tente novamente!'
    
    return f'Sua media foi {med:.1f}'


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

esc = input('Escolha o tipo de media que voce deseja:\nA-> aritmetica\nP -> Ponderada\n ')

print(medias(n1, n2, n3, esc))