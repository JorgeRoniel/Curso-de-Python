def triangulos(l1, l2, l3):
    if (l1 < 0) or (l2 < 0) or (l3 < 0):
        return 'Uma medida não pode ser um valor negativo, tente novamente!'
    
    else:
        if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
            if l1 == l2 == l3:
                return 'As medidas fornecidas são de um tringulo equilatero.'
        
            elif (l1 == l2) or (l2 == l3) or (l1 == l3):
                return 'As medidas fornecidas são de um tringulo isoceles.'
        
            else:
                return 'As medidas fornecidas são de um tringulo escaleno.'
        
        else:    
            return 'Esse não é um triangulo!'

lado1 = float(input('Digite um valor correspondente a um lado de um triangulo: '))
lado2 = float(input('Digite um segundo valor correspondente a um lado de um triangulo: '))
lado3 = float(input('Digite um ultimo valor correspondente a um lado de um triangulo: '))

result = triangulos(lado1, lado2, lado3)

print(result)
