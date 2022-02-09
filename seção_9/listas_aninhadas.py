"""
Listas aninhadas (Nested lists)

- Algumas linguagens possuem uma estrutura de dados chamados arrays:
    - Unidimensionais (arrays/vetores);
    - Multidimensionais (Matrizes).

- Em python, existem as listas!
- Listas aninhadas são listas de listas, ou array multidimensional em outras linguagens.

#Exemplo:

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3x3

#Acessando valores:

print(lista[0][1]) #2

#Iterando com listas aninhadas:
for x in lista:
    for num in x:
        print(num) #Imprime os numeros 

#List Comprehension
print()

[[print(valor) for valor in listas] for listas in lista]
"""



#Tabuleiro

tab = [[num for num in range(1, 4)] for valor in range(1, 4)]
print(tab)