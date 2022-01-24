"""
Modulo collection - Counter (contador)

collection -> High-performace Container Datetypes

Counter -> recebe um iteravel como parametro e cria um objeto do tipo collections counter, que é parecido
com um dicionario, tendo como chave o elemento da lista, e o valor, o numero d ocorrencias

#Como utilizar:
"""
#Exemplo

from collections import Counter

lista = [1, 2, 3, 4, 5, 1, 1, 3]

res = Counter(lista)

print(res)


