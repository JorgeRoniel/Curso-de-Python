"""
Função Reversed

Reversed != Reverse

- Reversed funciona com qualquer iteravel, diferente do reverse, que só funciona com listas
- Retorna um iteravel com o nome de List Reverse  iterator
- podemos converter o retorno para uma lista, tupla ou set
"""

#Exemplo 1:

lista = [num  for num in range(10)]
print(lista)
print(list(reversed(lista)))