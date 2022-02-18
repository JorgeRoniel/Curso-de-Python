"""
Modulo random

- Em Python, modulos são outros arquivos python.

random -> possui varias funções para a geração de numeros pseudo-aleatorios

- Existe 2 formas de utilizar o modulo, ou função deste.
    -Importanto todo o modulo
        import random

        #Exemplos - Importanto todo o modulo:
        print(random.random())
    -Importando uma função especifica
        from random import random
        #Exemplo - Importando uma função especifica.
        for x in range(10):
            print(random())

"""
from random import uniform
from random import randint
from random import choice
from random import shuffle

#Uniform() -> gera um numero pseudo-aleatorio entre numeros escolhidos:
print(uniform(2, 7))

#Randint() -> gera um valor inteiro pseudo-aleatorio entre os numeros escolhidos:
print(randint(2, 7))

#Choice() -> mostra um valor aleatorio em um iteravel:
jogo = ['Pedra', 'Papel', 'Tesoura']
print(choice(jogo))

#Shuffle() -> embaralha dados:
cartas = ['K', 'J', 'Q', 'Joker', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cartas)
shuffle(cartas)
print(cartas)