cam1 = input('Digite o caminho de um primeiro arquivo: ')
cam2 = input('Digite o caminho de um segundo arquivo: ')

with open(cam1, 'r') as arq1, open(cam2, 'r') as arq2, open('test5.txt', 'a') as arq3:
    ler1 = arq1.read()
    ler2 = arq2.read()

    arq3.write(ler1 + '\n')
    arq3.write(ler2)