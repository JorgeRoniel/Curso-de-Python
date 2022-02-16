"""
Debuggando com PDB

PDB -> Python Debugger

#Comandos basicos:

- l -> listar onde estamos no codigo
- n -> Proxima linha
- p -> imprime variavel
- c -> continua a execução/para o debugging

#OBS:
- A partir do Python 3.7, o PDB foi incorporado ao python como função integrada, não precisando mais importar a lib.
- breakpoint()
"""

#Debuggando com o Pycharm:

def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Valor Inválido!!'


print(divisao(10, 5))

#Debuggando com PDB

import pdb

a1 = 'Jorge'
b1 = 'Roniel'
pdb.set_trace()
nome_c = a1 + '' + b1

