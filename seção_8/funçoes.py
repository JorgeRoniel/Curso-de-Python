"""
Funções

- São pequenos trechos de codigos que realizam tarefas especificas;
- Ja utilizamos varias funções
#EX:
    print()
    map()
    len()

- Pode, ou não, receber parametros de entrada e retornar valores
- Muitos uteis para exercutar procedimentos similares por repetidas vezes

#OBS:
- Se escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma 
  verificação para que a função seja simplificada.

#Definição:

def nome_da_funçao(parametros_de_entrada):
    bloco_da_função/codigo_a_ser_executado



"""

#Exemplo de utilização:

#Forma 1 - funções 'globais'
cores =['verde', 'vermelho', 'laranja']
print(cores) #<- Função

#Forma 2 - funções reservadas a determinado type
cores.append('branco')
print(cores)

#Primeira Função:

def diz_oi():
    print('Olá!')

for n in range(3):
    diz_oi()

#Segunda Função:

def parabens():
    print('Parabens pra voce')
    print('Nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida!!!')

parabens()