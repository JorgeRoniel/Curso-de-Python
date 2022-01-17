ope = input('Digite a operação matematica desejada:\nSoma(s)\nSubtraçao(sub)\nMultiplicaçao(m)\nDivisao(d)\n')
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if ope == 's':
    soma = v1 + v2
    print(f'A soma dos valores informados é {soma}.')
elif ope == 'sub':
    subtracao = v1 - v2
    print(f'A subtraçao dos valores informados é {subtracao}.')
elif ope == 'm':
    multi = v1 * v2
    print(f'A multiplicaçao dos valores informados é {multi}.')
elif ope == 'd':
    divisao = v1 / v2
    print(f'A divisao dos valores informados é {divisao}.')
else:
    print('Houve algum problema, tente novamente!')