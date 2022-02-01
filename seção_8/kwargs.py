"""
Entendo sobre **kwargs

- Tem a mesma função do *args, porém ele recebe pparametros nomedados, e ao inves de
colocar em uma tupla, ele coloca em um dicionario.

#obs:
- tanto o *args, quanto o **kwargs não são obrigatorios;
- para desempacotar valores aqui, é so usar o asterisco duplo (**).
"""

#Exemplo 1: 

def cores(**kwargs):
    for p, c in kwargs.items():
        print(f'A cor preferida de {p.title()} é {c}')
    

cores(lucas='verde', jorge='preto', renato='cinza', jaqueline='azul')

#Exemplo 2:

def soma(a, b, c):
    return a + b + c

dicionario = dict(a=1, b=2, c=3) #OBS: o nome das chaves tem que ser os mesmos das variaveis da função.

print(soma(**dicionario))