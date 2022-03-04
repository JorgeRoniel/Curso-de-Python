"""
Leitura de Arquivos com Python

- Para ler o conteudo de um arquivo em python, usa-se a função open()

open() -> Na forma mais simples de usa-la, passamos apenas um parametro,
que neste caso é o caminho do arquivo. Essa função retorna um _ioTextIOwrapper
e é com ele que trabalhamos.

#OBS:
- Por padrão, a função open() abre o arquivo para leitura.
- Se o arquvo não existir, teremos o erro FileNotFoundError

"""

#Exemplo 1:

arquivo = open('arq1.txt')
#Para ler este conteudo, devemos usar a função read()

print(arquivo.read())

arquivo.close()