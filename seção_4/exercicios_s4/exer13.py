valor = float(input('Digite o valor da compra: '))
esc = input('Informe a forma de pagamento: parcelado(p) ou a vista (v)')


if esc == 'v':
    desconto = valor - (valor*10)/100
    newvalor = desconto - (desconto*5)/100
    print(f'O valor final a ser pago é: {newvalor} reais.')
elif esc == 'p':
    newvalor = valor - (valor*5)/100
    parcela = newvalor/3
    print(f'O valor da parcela ficara em 3 vezes de {parcela} reais.')
else:
    print('Forma de pagamento nao aceita, tente novamente.')