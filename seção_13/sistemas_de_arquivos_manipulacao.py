"""
Sistemas de Arquivo - Manipulação

"""
import os

#DEscobrindo se o arquivo existe:

print(os.path.exists('arq5.txt'))

#Criando Arquivos:

open('arq5.txt', 'w').close()

#ou

#os.mknod('arq6.txt') <- pode ser usado tambem

#Criando diretorios:

#os.mkdir('teste2')

#Renomeando arqquivos e diretorios:

#os.rename('teste2', 'teste_renamed')

#deletar arquivos:
os.remove('arq5.txt')

#Ao deletar um arquivo, eles não vão para a lixeira, eles somem.
#Deletando diretorios vazios:
os.rmdir('teste')

#OBS: se o diretorio não estiver vazio, da um error.
#