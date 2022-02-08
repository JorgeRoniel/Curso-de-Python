def piramide(n1, n2=0):
    j = 0
    i = 0
    
    while j <= n1:
        print('*' * j)
        if j == n1:
            i = j
        while i > n2:
            print('*' * (i-1))

            i -= 1

        
        j+=1

n1 = int(input('Entre com o numero para ser a altura do triangulo lateral: '))


piramide(n1)
