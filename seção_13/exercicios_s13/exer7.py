vogal = 'aeiouAEIOU'
cam = input('Digite o caminho de um arquivo: ')

with open(cam, 'r') as arq, open('test2.txt', 'w') as arq2:

    for linha in arq:
        for letra in linha:
            if letra in vogal:
                arq2.write('*')
            else:
                arq2.write(letra)
