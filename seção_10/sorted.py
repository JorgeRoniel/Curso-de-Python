"""
Função Sorted

- Serve para ordenar elementos
- Funciona com qualquer tipo de iteravel
- Retorna uma lista com os elementos do iteravel em ordem

"""

lista = [9, 7, 4, 3, 5, 1]

print(sorted(lista))

#Adicionado parametros no sorted()
print(sorted(lista, reverse=True))

#Exemplo:

musics = [
    {'Track': 'Look at Me', 'Repeats': 300},
    {'Track': 'SAD!', 'Repeats': 550},
    {'Track': 'Jocelyn Flores', 'Repeats': 400},
    {'Track': 'I dont do this anymore', 'Repeats': 200},
    {'Track': 'Moonligth', 'Repeats': 500}
]

#Ordena da musica com mais 'Repeats' até a com menos 'Repeats'.
print(sorted(musics, key=lambda music: music['Repeats'], reverse=True))


#LLJ
