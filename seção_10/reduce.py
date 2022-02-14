"""
Função Reduce

- A partir do python3+, essa função não é mais uma função integrada
- Agora temos que importar e utilizar essa função a partir do modulo "functools"
- A função recebe dois parametros, uma função e um iteravel

"""

#Exemplo:

from functools import reduce


dados = [1, 2, 3, 4, 5, 6]


def soma(a, b):
    return a + b


res1 = reduce(soma, dados)

print(res1)

"""O reduce pega os dois primerios valores, soma, guarda o resultado, e soma o resultado com o proximo elemento, até o
fim da lista"""