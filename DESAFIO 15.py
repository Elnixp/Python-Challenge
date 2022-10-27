dias = int(input('Quantos dias o carro ficou alugado?: '))
km = float(input('Quantos Km percorridos?: '))
valor = dias*60 + km*0.15
print('O valor a ser pago é {:.2f} R$'.format(valor))
