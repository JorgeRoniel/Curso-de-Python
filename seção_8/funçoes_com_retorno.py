"""
Funções com Retorno:

- Funções que retornam valores, usam a palavra reservada 'return'

OBS:
- Não precisamos necessariamente criar uma variavel para receber o retorno de uma função,
  poddemos utilizar outras funções para passar a execução da nossa função.

#Sobre a palavra return:

1- Ela finaliza a função
2- Pode haver mais de um return em uma função, mas so um sera executado
3- podemos retornar qualquer tipo de dado, e multiplos valores
"""

#Exemplos:

def quadrado_de_sete():
    return 7 ** 2

ret = quadrado_de_sete()
print(ret)

#ou

print(quadrado_de_sete())