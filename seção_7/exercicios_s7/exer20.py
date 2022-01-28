lista = []
lista_impar = []

for x in range(0, 10):
    num = int(input('Insira um numero que esteja no intervalo entre 0-50: '))
    if num > 50 or num < 0:
        print('Valor Fora do Intervalo Estipulado!')
    else:
        lista.append(num)
        if num % 2 == 1:
            lista_impar.append(num)
        

print(lista)
print(lista_impar)
