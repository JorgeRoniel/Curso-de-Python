def piramide(n1, n2=0):
    list(print(' ' * (n1 - i) + ('*' * (2 * i - 1))) for i in range(1, n1+1))
 


n1 = int(input('Entre com o numero para ser a altura do triangulo lateral: '))


piramide(n1)