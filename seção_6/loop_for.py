"""
Loop for 

for -> estrutura de repetição

for item in interavel:
    loop

usamos loops para iterar sobre sequencias ou valores iteraveis

ex: 
- strings
    name = 'jorge'
- listas
    lista = [1, 2, 3, 4, 5]
- range
    num = range(1, 10)

OBS: quando nao queremos usar um valor, usamos o underline
"""

#exemplo for 1 (iterando sobre uma string)

nome = 'Jorge Roniel'
lista = [1, 2, 3, 4, 5, 6]
num = range(1, 10)

for letra in nome:
    print(letra, end='') #imprimndo sem quebra de linha
print('')
#exemplo for 2 (iterando sobre uma lista)

for numero in lista:
    print(numero)
print('')
#exemplo for 3 (iterando sobre um range)

for num in range(1, 10):
    print('')
    print(num)
print('')
#enumarated

for valor in enumerate(nome):
    print(valor)
print('')
#usuario informa a quantidade do loop

qtd = int(input('Quantas vezes o loop vai girar? '))

for n in range(1, qtd):
    print(f'Imprimindo {n}')

#colocando emojis

#original U+1F603
#modificado U0001F603

for num in range(1, 11):
    print('\U0001F603' * num)