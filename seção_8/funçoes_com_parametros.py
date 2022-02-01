"""
Funções com parametros de entrada

- Recebem dados para serem processados dentro da mesma


"""

#Exemplo:

def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

lista = []


for x in range(0, 3):
    num = int(input('Digite um Numero: '))
    lista.append(num)

med = media(lista[0], lista[1], lista[2])
print(f'Sua media é: {med:.1f}')