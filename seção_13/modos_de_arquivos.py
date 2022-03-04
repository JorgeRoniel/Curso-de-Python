"""
Modos de abertura de arquivos

R -> abre para leitura - Padrão
W -> abre para a escrita, se o arquivo não existir, ele cria, senão ele sobrescreve.
X -> abre para escrita somente se o arqivo não existir
A -> abre para escrita, adicionando o conteudo ao final do arquivo.
+ -> abre para o modo de atualização: Leitura e Escrita
"""

with open('arq4.txt', 'a') as arq:
    while True:
        dados = input('Digite qualquer coisa, caso queira sair, digite "sair": ')
        if dados != 'sair':
            arq.write(dados)
            arq.write('\n')
        else:
            break

