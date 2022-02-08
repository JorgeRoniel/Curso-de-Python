def volume_esfera(r):
    vol = (4 * 3.14 * r) / 3
    return vol

raio = float(input('Entre com um valor para o raio de uma esfera, para o calculo de seu volume seja feito: '))
volume = volume_esfera(raio)

print(f'O volume da esfera cujo raio é {raio}, é: {volume:.1f}')