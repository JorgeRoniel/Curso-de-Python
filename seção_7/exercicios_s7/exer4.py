lista = []

for i in range(0, 8):
    num = int(input('Digite um numero: '))
    lista.append(num)

n1 = int(input('Insira dois valores para index da lista: '))
n2 = int(input('Agora, insira o segundo valor: '))

soma = lista[n1] + lista[n2]

print(f'A soma dos valores cujo index foi informado acima é {soma}')
