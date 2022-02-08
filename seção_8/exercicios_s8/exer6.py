def conversao_segundos(h, m, s):
    conv_m = m * 60
    conv_h = h * 3600
    total = conv_m + conv_h + s

    return total

horas = int(input('Digite aqui as horas: '))
minutos = int(input('Digite aqui os minutos: '))
segundos = int(input('Digite aqui os segundos: '))

conv = conversao_segundos(horas, minutos, segundos)

print(f'O total de segundos é: {conv}')