def calculadora(n1, n2, *args):
    if '+' in args:
        soma = n1 + n2
        return f'A soma dos numeros é {soma}'
    
    elif '-' in args:
        sub = n1 - n2
        return f'A subtração dos numeros é {sub}'

    elif '*' in args:
        mult = n1 * n2
        return f'A multiplicação dos numeros é {mult}'
    
    elif '/' in args:
        div = n1 / n2
        return f'A divisão dos numeros é {div:.1f}'
    
    return 'Sinal desconhecido, tente novamente.'

print('-=' * 20)
print('Bem vindo a calculadora em Python!\nDigite dois valores e escolha a operação desejada.')
print('-=' * 20)
print('')

n1 = float(input('Entre com o primeiro valor: '))
n2 = float(input('Digite agora o segundo valor: '))
esc = input("Informe a operação desejada:\n'+' -> Adição\n'-' -> Subtração\n'*' -> Multiplicação\n'/' -> Divisão\n")

result = calculadora(n1, n2, esc)

print(result)