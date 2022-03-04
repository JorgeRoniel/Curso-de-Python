"""
Escrevendo em arquivos

#OBS:
- Ao abrirmos um arquivo em modo de leitura, não podemos escrever nele, apenas ler. Isso tambem
ocorre do mesmo jeito, ao inverso.
- Ao abrir um arquivo para escrita, se não existir, ele é criado.
"""

#Exemplo:

with open('arq2.txt', 'w') as archive:
    archive.write('Escrevendo dados em um arquivo via Python,\n')
    archive.write('Its Very Easy.')


#Pegando dados do usuario e registrando em outro arquivo:

with open('Dados.txt', 'w') as arq:
    while True:
        dados = input('Digite qualquer coisa: ')
        arq.write(dados)
        arq.write('\n')
        esc = input('Deseja continuar? S/N')
        if esc == 'N':
            break
        else:
            continue
