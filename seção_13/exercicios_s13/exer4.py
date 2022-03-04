vogal = 'aeiouAEIOU'
cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

with open('..\\arq1.txt', 'r') as arq:
    ler = arq.read()

    print(f'O numero de vogais no arquivo é: {len([lambda i: i for i in ler if i in vogal])}')
    print(f'O numero de consoantes no arquivo é: {len([lambda x: x for x in ler if x in cons])}')
