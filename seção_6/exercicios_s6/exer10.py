lista_par = []
c = 0

while c < 50:
    c += 1
    if c % 2 == 0:
        lista_par.append(c)
        soma = sum(lista_par)
    else:
        continue

print(soma)