cam = input('Digite o caminho de um arquivo desejado:')
new = input('Agora, insira o nome de um novo arquivo: ')

with open(cam, 'r') as arq1, open(new, 'a') as arq2:
    ler = arq1.read()
    upper = ler.upper()

    arq2.write(upper)