import math

def fatorial(num):
    #fat = math.factorial(num)
    
    fat = 1
    for x in range(1, num+1):
        fat *= x
    
    return f'O fatorial do numero informado é {fat}'

num = int(input('Entre com um numero para calcular seu fatorial: '))

res = fatorial(num)

print(res)