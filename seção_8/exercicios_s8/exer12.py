def soma_alg(num):
    if num < 0:
        return 'Valor Inválido, Tente novamente!'
    
    x = [int(a) for a in str(num)]
    soma = sum(x)
    return f'A soma dos algarismos do numero digitado é {soma}'

print(soma_alg(521))