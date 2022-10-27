velocidade = float(input('Qual a velocidade em Km/h: '))
if velocidade >= 80:
    multa = (velocidade - 80)*7
    print('Parabéns campeão! você acaba de ser multado, o limite dessa via é 80Km/h '
          'você estava a {}Km/h e terá que pagar a bagatela de {:.2f} Reais'.format(velocidade, multa))
else:
    print('Tudo em ordem.')
