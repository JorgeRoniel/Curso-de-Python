"""
Função len

len() -> retorna o numeros de itens de um iteravel
"""

#Exemplo:

lista = [num for num in range(11)]
print(len(lista))

"""
Função Abs

abs() -> retorna o valor absoluto de um numero inteiro ou real. Basicamente, seria o seu valor sem o sinal

"""

#Exemplo:

print(abs(-5))
print(abs(5))
print(abs(-7.7))
print(abs(7.7))

"""
Função Sum

sum() -> recebe um iteravel, podendo receber um valor incial, e retorna a soma total dos valores, incluido o valor inicial

"""

#Exemplo:

print(sum([1, 2, 3, 4, 5])) #15
print(sum([1, 2, 3, 4, 5], 5)) #20

"""
Função Round

round() -> retorna um numero arredondado para n digitos de precisão após a casa decimal, se a precisão
não for informada, ele retorna um numero inteiro mais proximo da entrada.

"""

#Exemplo:

print(round(10.5)) #10
print(round(1.234563839375, 1)) #1.2
print(round(10.1212121121221212, 2)) #10.12
print(round(10.8)) #11