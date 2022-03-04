"""
StringIO

- Para ler e escrever em um arquivo, o software deve ter permissões para isso.
StringIO -> utilizado para ler e criar arquivos em memoria.
- Podemos criar um arquivo em memoriaja com uma string inserida, ou mesmo vazio, para inserirmos depois.
"""

from io import StringIO

msg = 'Olá, tudo bem?'

archive = StringIO(msg)
print(archive.read())