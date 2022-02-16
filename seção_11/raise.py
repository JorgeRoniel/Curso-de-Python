"""
Levantando os proprios erros com raise

raise -> lança excessões, não é uma função, é uma palavra reservada.

- é util para criar nossas proprias excessões e mensagens de error.

#Utilização:

raise TipodoErro('mensagem do erro')

EX:

raise NameError('Você é louquinho da cabeça, mano!')

"""



#Exemplo 2:

def texto_colorido(texto, cor):
    if type(texto) is not str:
        raise TypeError('A variavel deve receber uma string!')
    if type(cor) is not str:
        raise TypeError('A variavel deve receber uma string!')
    print(f'O texto {texto}, sera impresso na cor {cor}!')

texto_colorido('oi', 3)