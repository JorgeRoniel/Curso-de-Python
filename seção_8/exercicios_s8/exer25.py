def expressao_mat(num):
    exp = (2/4) + (5/5) + (10/6) + (((num**2) + 1)/(num + 3))

    return f'O resultado da exepressão matemática é {exp:.1f}'

num = int(input('Entre com um valor: '))
res = expressao_mat(num)

print(res)