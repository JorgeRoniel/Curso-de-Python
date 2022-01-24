"""
Listas:

listas funcionam como arrays em outras linguegens de programaçao

são dinamicas, e tambem recebem qualquer tipo de dado

em C/Java, arrays sempre tem tipo e tamanho fixos!!

- Dinâmico:
    não possui tamanho fixo

as listas em python são representadas por '[]'
ex: 

lista = []

- OBS: Listas aceitam repetições!!!

"""

lista = list(range(11))

print(lista)

#checar se determinado valor esta na lista

if 10 in lista:
    print('sim')
else:
    print('nao')

#ordernar uma lista

lista2 = [34, 300, 10, 1, 2, 44, 30, 777]

lista2.sort()

print(lista2)

#fazer a contegem de ocorrencias de certo valor dentro da lista

print(lista2.count(10))

#adicionar elementos na lista

lista.append(777) #o append so adiciona um valor por vez
lista.append([0, 38, 778])
print(lista)

lista2.extend([11, 123, 1000, 'jr'])
print(lista2)

#Adicionando um elemento com seu respectivo indice

lista.insert(3, 'Jorge')
print(lista)

#copiar uma lista

lista3 = lista.copy()
print(lista3)

#tamanho das listas

print(len(lista))

#removendo o ultimo elemento
#OBS: para remover pelo indice, é so colocar o indice no pop()
lista3.pop()
print(lista3)

#para limpar a lista, é so usar o .clear()

#transformando string em lista

nome = 'Jorge Roniel'
print(nome)
nome = nome.split()
print(nome)

#Soma, maior valor, menor valor

lista4 = [1000, 2, 300, 44, 123]

print(max(lista4)) #maior valor
print(min(lista4)) #minimo valor
print(sum(lista4)) #soma

#copiando uma lista para outra (shalow copy e deep copy)

# Deep Copy
nova = lista4.copy()
print(nova)

#na copia acima, ambas as lista ficaram independentes, nao havendo modificações em nenhuma das dua
#isso, em python, se chama deep copy


# Shallow Copy

lista5 = [1, 2, 3, 9, 8, 7]

new = lista5

new.append(5)

print(new)

#na copia acima, quando ha uma modificação em uma das listas, a outra se modifica tambem
#isso, em python, se chama shallow copy