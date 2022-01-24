"""
Collections - default dict

Default Dict -> ao criar um dicionario, nos informamos um valor default,
podendo utilizar um lambda pra isso. Esse valor sera utilizado sempre que
não houver um valor definido.

#OBS:
- no Default dict não existe o Keyerror
- Lambdas são funções sem nome que podem, ou não, receberem parametros de entrada e retornar valores.


"""

#Como usar:

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['Nome'] = 'Jorge Roniel'

print(dicionario)
print(dicionario['outro'])