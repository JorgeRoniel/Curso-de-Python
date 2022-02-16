"""
Bloco Try - Except

-  utilizamos esse bloco para tratar erros que podem acontecer no nosso codigo
evitando que o programa pare, ou o usuario receba mensagens de erros inesperados.

- Forma de usar:

try:
    //problema
except:
    //o que deve ser feito caso ocorra o problema.

- Tratar um erro de forma generica não é a melhor forma. O modo correto é ser mais especifico.

#Exemplo 1 - Erro generico:

try:
    funcao()
except:
    print('Errouuu')

#Exemplo 2 - Tratado de forma mais especifica:

try:
    funcao()
except NameError:
    print('Você está tendando usar uma função inexistente.')

#Exemplo 3 - Tratado de forma mais especifica com detalhes do erro:

try:
    funcao()
except NameError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

#Exemplo 4 - Tratando varios erros:

try:
    #gues() -> NameError
    #len(4) -> TypeError
    #print('ges'[10]) -> deu problema
except NameError as erra:
    print(f'O erro foi: {erra}')
except TypeError as errb:
    print(f'O erro foi: {errb}')
except:
    print('Deu problema!')
"""



"""

Else e Finally

Else -> é executado apenas se não ocorrer o erro.
Finally -> é sempre executado, com erro ou não.
"""

try:
    num = int(input('Digite um número: '))

except ValueError:
    print('Valor errado!')
else:
    print(f'O numero digitado foi {num}')