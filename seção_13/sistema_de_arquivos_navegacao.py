"""
Sistema de Arquivos - Navegação

- Para fazer uso e manipulação de arquivos no sistema operacional, precisamos
importar e fazer uso do modulo 'OS'

os -> Operating System
"""

import os

#getcwd() -> pega o current work directory (Diretorio atual)
print(os.getcwd())

#chdir() -> Muda o diretorio
os.chdir('..')
print(os.getcwd())

#name() -> mostra qual sistema operacional o programa está rodando.
print(os.name) #nt(windows) | posix (linux ou mac)

res = os.path.join(os.getcwd(), 'seção_13', 'teste')
os.chdir(res)

print(os.getcwd()) #C:\Users\jorge\OneDrive\Área de Trabalho\Curso Python 2k22\seção_13\teste

#listdir() -> podemos listar todos os modulos e diretorios

os.chdir('..')
scanner = os.listdir()

print(len(scanner))


