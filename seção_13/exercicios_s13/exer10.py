cam = input('Digite o caminho de um arquivo: ')
maiores = []
cad = dict()

with open(cam, 'r') as arq1, open('test7.txt', 'a') as arq2:
    ler = arq1.readlines()

    for dado in ler:
        dado_sep = dado.split(':')
        maiores.append(int(dado_sep[1]))
        cad.update({f'{dado_sep[0]}': int(dado_sep[1])})

    for key, value in cad.items():
        if int(value) == max(maiores):
            arq2.write(f'{key}: {value}')