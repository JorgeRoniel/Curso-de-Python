from itertools import count


qtd = int(input('Informe quantas vezes o loop deve ser executado: '))

lista = []

for c in range(0, qtd):
    n = int(input('Digite um numero: '))
    lista.append(n)
    maior  = max(lista)
    cont = lista.count(maior)

print(f'O maior valor digitado foi {maior}, e a quantidade de vezes que ele apareceu foi {cont}')