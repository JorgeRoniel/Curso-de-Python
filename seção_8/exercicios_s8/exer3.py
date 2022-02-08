def positivo_negativo(num):
    if num < 0:
        return '-1'
    elif num > 0:
        return '1'
    return '0'

num = int(input('Digite um numero: '))
res = positivo_negativo(num)

print(res)