"""
Tipo string:

todo valor que estiver entre aspas
ex: '1', 'ola', 'true', 'false', etc...

alguns metodos com strings:

upper()
lower()
title()
split()

"""

name = input('put here your name: ').title()

print(f'{name}, do you love me? Are you ridding?')


name2 = 'drake'

print(name2[0:3]) #slice de string
print(name2.split())
print(name2[::-1])
print(name2.replace('d', 'b'))

text = 'socorram me subino onibus em marrocos' #palindromo kkkk

print(text)
print(text[::-1])