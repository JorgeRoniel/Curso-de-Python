def consumo_gasosa(km, l):
    consumo = km / l
    if consumo < 8:
        return 'Venda o carro!'
    
    elif consumo > 8 and consumo < 14:
        return 'Econômico!'
    
    elif consumo > 14:
        return 'SuperEconômico!!!'
    
    return 'Algo de errado não está certo, tente novamente!'

km = float(input('Informe quantos quilometros(KM) foram percorridos: '))
l = float(input('Agora, informe quantos litros foram consumidos nessa viagem: '))

cons = consumo_gasosa(km, l)

print(cons)