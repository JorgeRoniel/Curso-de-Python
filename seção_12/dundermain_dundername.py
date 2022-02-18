"""
Dunder Main e Dunder Name

- Dunder == '__'
- Dunder main -> __main__
- Dunder name -> __name__

- No python, são utilizados dunder para criar funções, atributos, propriedades e etc. Utilizando
Dunder para não gerar coflito na programação.

- Em Python, ao executar um modulo diretamente na linha de comando, internamente o Python
atribuira à variavel __name__ o  valor __main__, indicando que esse modulo é o mudulo de
execução principal.


"""

from cod_pronto import maior_fator

print(maior_fator(100))