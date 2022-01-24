"""
Tuplas 

São bastantes parecidas com as listas, as principais diferenças são:

1- representadas por '()'
2- são imutaveis, ou seja, ao cria-la, ela não muda, uma operação em uma tupla gera outra tupla
3- São definidas pela virgula

#OBS1:

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
                            #ambas são tuplas
tupla2 = 1, 2, 3, 4, 5
print(tupla2)

#OBS2: 

tupla3 = (4) #não é uma tupla

tupla4 = (4, ) #é uma tupla

#Gerando tupla com range

tupla = tuple(range(1, 20))
print(tupla)

#Desempacotamento de elementos da tupla

tupla_nome = ('Jorge', 'Roniel')

nome, sobrenome = tupla_nome

print(nome)
print(sobrenome)

#Soma, valor maximo e valor minimo é igual nas listas, usando os mesmos metodos

#Concatenação de Tuplas

tupla1 = 1, 2, 3
tupla2 = 4, 5, 6

tupla3 = tupla1 + tupla2

print(tupla3)

#Tuplas sao imutaveis, mas podemos sobrescrever seus valores

#Usamos tuplas sempre que nao precisarmos mudar a coleção

#Na tupla não temos o Shallow Copy
"""

