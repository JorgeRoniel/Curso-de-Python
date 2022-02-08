def desenha_linha(num):
    return '=' * num

num = int(input('Informe quantas vezes voce quer que o sinal "=" seja repetido na tela: '))

res = desenha_linha(num)
print(res)