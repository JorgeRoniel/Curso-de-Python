lista = []

for x in range(0, 5):
    num = float(input('Digite um Numero: '))
    lista.append(num)

cod = int(input('Insira um codigo (0 a 2):\n0 - Finaliza o programa.\n1 - Mostra a lista de todos os valores informados.\n2 - Mostra a mesma lista, mas ao inverso.'))

if cod == 1:
    print(lista)
elif cod == 2:
    print(lista[::-1])
elif cod == 0:
    quit()
else:
    print('Codigo Invalido!')
    