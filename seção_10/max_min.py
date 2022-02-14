"""
Funções Max e Min

max() -> retorna o maior valor dentro de um iteravel ou o maior de 2 ou mais elementos

"""

#Exemplo 1:

lista = [num for num in range(10)]

print(max(lista)) #9

#Exemplo 2:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))


print(f'O maior numero digitado foi {max(n1, n2)}')

"""
Min() -> retorna o menor valor dentro de uma iteravel ou o menor entre 2 numeros ou mais
"""

#Exemplo 1:

lista = [num for num in range(10)]

print(min(lista)) #0

#Exemplo 2:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))


print(f'O menor numero digitado foi {min(n1, n2)}')

#Exemplo 3:

musics = [
    {'Track': 'Look at Me', 'Repeats': 300},
    {'Track': 'SAD!', 'Repeats': 550},
    {'Track': 'Jocelyn Flores', 'Repeats': 400},
    {'Track': 'I dont do this anymore', 'Repeats': 200},
    {'Track': 'Moonligth', 'Repeats': 500}
]

print(max(musics, key=lambda music: music['Repeats'])['Track'])
print(min(musics, key=lambda music: music['Repeats'])['Track'])

#Encontrando a música mais tocada sem o max(), e sem lambda

maior = 0

for music in musics:
    if music['Repeats'] > maior:
        maior = music['Repeats']

for music in musics:
    if music['Repeats'] == maior:
        print(music['Track'])
