"""
Entendo o *args

- O *args é um parametro como qualquer outro, isso significa que poderemos chama-lo 
de qualquer coisa, desde de que começe com um asterisco(*).
- Mas por concessão, chamamos de *args

- O parametro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla, então desde ja, a tupla é imutável.

- Com ele, não precisamos limitar quantos argumentos uma funçao pode receber
"""

#Exemplo 1:

def soma(*args):
    return sum(args)

print(soma(1, 3, 9))

#Exemplo 2:

def login(*args):
    if 'Jorge' in args:
        return 'Bem vindo!!'
    return 'ERROR!!!'

print(login('João'))
print(login('Jorge'))

#Exemplo 3 (Desempacotador):

lista = [1, 2, 3, 4, 5, 6]

# print(soma(lista)) #TypeError
print(soma(*lista))

"""
OBS: O asterisco é usado para informar que estamos psaando como parametro uma
coleção, então ele fará um desempacotamento antes.
"""