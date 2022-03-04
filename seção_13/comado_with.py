"""
Bloco With

- É utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados apos o bloco with

"""

#Exemplo:

with open('arq1.txt') as arquive:
    print(arquive.read())


#É a forma pythonica para se trabalhar com arquivos.
