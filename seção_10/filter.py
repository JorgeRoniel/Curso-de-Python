"""
Função Filter

- filtra dados de uma derterminada coleção.
- a função filter tambem recebe dois parametros, uma função e um iteravel.
- A diferença entre o map() e o filter() é:
    - O map() recebe dois parametros e retorna um objeto mapeando a função para cada objeto do iteravel.
    - O filter() recebe dois parametros e retorna filtrando apenas os elementos de acordo com a função.


"""
#Exemplo 1:

import statistics

valores = [1, 3, 4, 5, 6]
media = statistics.mean(valores)

print(list(filter(lambda x: x > media, valores))) #[4, 5, 6]

#Exemplo 2:

paises = ['', 'brasil', '', 'alemanha', 'Chile', 'Suecia', '', '', 'Inglaterra']

res = filter(None, paises) #Filtra e retira os valores vazios

print(list(res))