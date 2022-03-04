arqu = input('Digite um path para um arquivo de texto: ')

with open(arqu, 'r') as arq:
    print(len(arq.readlines()))