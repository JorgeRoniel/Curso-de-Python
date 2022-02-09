"""
List Comprehensions

- Utilizando o list comprehension, podemos criar novas listas com dados processados 
a partir de outro iteravel.

#Sintaxe: 

[dado for dado in iteravel]

- Nos podemos utilizar estruturas condicionais logicas nas nossas list comprehension

"""

#Exemplo 1:

num = [1, 2, 3, 4, 5]

res = [numeros * 10 for numeros in num]
print(res)

#Exemplo 2:

def ao_quadrado(num):
    return num ** 2


print([ao_quadrado(numeros) for numeros in num])

#Exemplo 3:

pares = [numeros for numeros in num if numeros % 2 == 0]
impares = [numeros for numeros in num if numeros % 2 != 0]

print(pares)
print(impares)