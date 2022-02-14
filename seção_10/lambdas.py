"""
Lambdas

- São funções sem nome, ou seja, funções anônimas.
- Podemos ter funções lambdas com multiplos parametros

"""
#Exemplo de função lambda

lam = lambda x: 3 * x + 1
print(lam(4))

#Exemplo 2:

nome = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome('jorge', 'roniel'))

#Exemplo 3:

media = lambda n1, n2, n3: (n1 + n2 +n3) / 3
print(media(9, 10, 8))

#Exemplo 4:

def gerador_de_função_quadrada(a, b, c):
    """Gera e calcula uma função do tipo de f(x) = ax² + bx + c"""

    return lambda x: (a*(x**2)) + (b*x) + c

teste = gerador_de_função_quadrada(2, 3, -5) #Aqui passamos os parametros da função principal
print(teste(2)) #Aqui passamos o parametro da lambda

print(gerador_de_função_quadrada(3, 4, -8)(3)) #Podemos fazer assim tambem.