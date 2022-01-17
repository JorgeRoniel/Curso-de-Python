"""
Loop while

while expressao_booleana:
    //loop
    //incremento(ou decremento)

enquanto for true, ele vai continuar rodando

OBS: sempre se ligar no criterio de parada, senao vira um loop infinito...

Break

utilizamos break para sair de um loop de maneira projetada


"""

n = 0
while n < 5:
    print(n)
    n = n+1
print('')
v = ''
while v != 'sim':
    v = input('Ja acabou, jessica? ')

c = 0
while c < 10:
    c += 1
    if c == 7:
        break
    else:
        print(c)
print('sai do loop')
