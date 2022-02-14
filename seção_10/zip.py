"""
Função Zip

zip() -> cria um iteravel (Zip Object) que agrega elementos de cada um dos iteraveis passados como entrada em pares.

#OBS:
- Se estiver trabalhando com iteraveis de tamanhos diferentes, irá parar de agregar quando o numero de elementos
do menor iteravel acabar.
- podemos utilizar com o zip() diferentes tipos de iteraveis.

"""

#Exemplo 1:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

res = zip(lista1, lista2)
print(list(res)) #[(1, 4), (2, 5), (3, 6)]

#Exemplo 2:

notas1 = [10, 9, 5]
notas2 = [4, 9, 10]
alunos = ['Pedro', 'Maria', 'João']

final = {dados[0]:max(dados[1], dados[2]) for dados in zip(alunos, notas1, notas2)}

print(final)