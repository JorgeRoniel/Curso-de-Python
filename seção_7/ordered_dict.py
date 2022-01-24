"""
Modulo Collections: Ordered Dict

- No dicionario comum, não garante a ordem de inserção de elementos

Ordered Dict -> É certeza manter a ordem na inserção

"""

#Como Usar:

from collections import OrderedDict

dicionario = OrderedDict({'a': '1', 'b': '2', 'c': '3'})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}; Valor = {valor}')