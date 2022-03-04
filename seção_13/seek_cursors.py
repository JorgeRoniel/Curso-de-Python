"""
Seek and Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo. Ela recebe com parametro que indica onde queremos
clocar o cursor.

"""

#Exemplo:

arquivo = open('arq1.txt')
#arquivo.seek(22)
#print(arquivo.read())

#ReadLine() -> Função que le o arquivo linha a linha.
print(arquivo.readline())

#readlines()

"""
Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco do pc
e o nosso programa. Essa conexão é chamada streaming. Ao finalizar, devemos fechar essa conexão usando 
a função close(). 
"""

arquivo.close()