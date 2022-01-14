salario = float(input('Informe o seu salario: '))
emprestimo = float(input('Informe o valor do emprestimo a ser feito: '))

porcen = (salario*20)/100

if emprestimo > porcen:
    print('Emprestimo nao concedido!')
else:
    print('Emprestimo concedido!')
