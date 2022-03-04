cam = input('Digite o caminho do arquivo de texto desejado: ')

with open(cam, 'r') as arq:
    ler = arq.read()

    for x in 'abcdefghijklmnopqrstuvwwxyz':
        print(f'O caracter {x} aparece {ler.count(x)} vezes.')