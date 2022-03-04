with open('test.txt', 'w') as arq:
    while True:
        dados = input('Digite alguma coisa para ser gravada em um arquivo de texto.\nCaso queira parar digite "0":\n')
        if dados != '0':
            arq.write(dados)
        else:
            break

with open('test.txt', 'r') as arq:
    print(arq.read())