"""
Funções Any e All

All -> Retorna true se todos os elementos do iteravel forem verdadeiros ou mesmo se ele estiver vazio.


"""

#Exemplo:

print(all([0, 1, 2, 3, 4])) #False
print(all([])) #True
print(all([1, 3, 4, 5, 6, 7])) #True

"""
Any -> Retorna true se qualquer elemento do iteravel for verdadeiro, se estiver vazio, retorna false

"""

#Exemplo:

print(any([0, 1, 2, 3, 4])) #True
print(any([])) #False
print(any([1, 3, 4, 5, 6, 7])) #True
print(any([0, 0, 0, 1, 0, 0, 0])) #True