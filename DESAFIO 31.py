distancia = float(input('Qual a distância da viagem em Km?: '))
if distancia <=200:
    valor = distancia * 0.50
    print('O valor da passagem será de {:.2f} Reais'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da passagem será de {:.2f} Reais'.format(valor))