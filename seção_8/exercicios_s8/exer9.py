def volume_cil(h, r):
    pi = 3.141592
    vol = pi * (r ** 2) * h

    return vol

h = float(input('Digite um valor para a altura do cilindro: '))
r = float(input('Agora, digite um valor para o raio de sua base: '))

res = volume_cil(h, r)

print(f'O volume do cilindro é: {res:.2f}cm³')