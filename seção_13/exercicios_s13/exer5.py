cam = input('Digite o caminho do arquivo de texto desejado: ')
car = input('Agora, digite uma letra:')

with open(cam, 'r') as arq:
    ler = arq.read()

    if car in ler:
        print(ler.count(car))