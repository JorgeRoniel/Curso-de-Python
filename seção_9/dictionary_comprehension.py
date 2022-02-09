"""
Dictionary Comprehension

- Mesma função da list comprehension

#Sintaxe:

{chave:valor for valor in iteravel}
"""

#Exemplo 1:

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

num_quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(numeros)
print(num_quadrado)

#Exemplo 2:

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mix = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mix)