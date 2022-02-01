"""
Funções com parametros padrão

- Funções onde a passagem de parametro é opcional.
- EX:
    print()


"""

def media(n1=0, n2=0, n3=0):
    return (n1 + n2 + n3) / 3

print(10 * '-=')
med = media()
print(f'Sua media é: {med:.1f}')
print(10 * '-=')
print('')