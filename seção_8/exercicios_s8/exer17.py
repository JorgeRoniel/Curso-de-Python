def somatorio_entre(n1, n2):
    lista = []
    for x in range(n1, n2):
        lista.append(x)
    
    soma = sum(lista)
    return f'A soma dos numeros entre {n1} e {n2} é: {soma}'

n1 = int(input('Entre com um numero: '))
n2 = int(input('Agora, entre com outro numero: '))

result = somatorio_entre(n1, n2)
print(result)