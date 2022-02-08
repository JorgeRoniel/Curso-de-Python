def maior_fator(num):
    fatores = []
    fat_primos = []

    for c in range(2, num):
        if (num % c) == 0:
            fatores.append(c)
    for elementos in fatores:
        cont = 0
        for x in range(2, elementos):
            if (elementos % x) == 0:
                cont += 1
        
        if cont == 0:
            fat_primos.append(elementos)
    if len(fat_primos) == 0:
        return f'O maior fator primo de {num} é {num}'
    return f'O maior fator primo de {num} é {max(fat_primos)}'
    
result = maior_fator(100)

print(result)
