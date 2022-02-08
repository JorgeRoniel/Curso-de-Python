def conversor_temp(c):
    conv_f = c * (9/5) + 32

    return conv_f

celsios = float(input('Digite um valor para a temperatura em graus celsios: '))
conv = conversor_temp(celsios)

print(f'A temperatura informada acima, convertida para Fahrenheit é: {conv:.1f} F°')