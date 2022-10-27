from time import sleep
print('Elabore um programa que calcule o valor a ser pago por um produto, '
      'considerando seu preço normal e a condição de pagamento.\n'
      '* À vista dinheiro/cheque: 10% de desconto\n'
      '* À vista no cartão: 5% de desconto\n'
      '* Em até 2x no cartão: preço normal\n'
      '* 3x ou mais no cartão: 20% de juros')
valor = float(input('Qual o valor do produto em Reais?'))
sleep(1)
print('Qual será a forma de pagamento escolha:\n'
      '1 - À vista dinheiro/cheque: 10% de desconto\n'
      '2 - À vista no cartão: 5% de desconto\n'
      '3 - Em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros\n')
a = 'À vista dinheiro/cheque: 10% de desconto'
b = 'À vista no cartão: 5% de desconto'
c = 'Em até 2x no cartão: preço normal'
d = '3x ou mais no cartão: 20% de juros'
pagamento = int(input('Forma de pagamento: '))
if pagamento == 1:
    valor = valor * 0.9
    print('Utilizando o forma de pagamento {}, sua compra terá o valor de {:.2f}R$'.format(a, valor))
elif pagamento == 2:
    valor = valor * 0.95
    print('Utilizando o forma de pagamento {}, sua compra terá o valor de {:.2f}R$'.format(b, valor))
elif pagamento == 3:
    valor = valor * 1
    print('Utilizando o forma de pagamento {}, sua compra terá o valor de {:.2f}R$'.format(c, valor))
elif pagamento == 4:
    valor = valor * 1.2
    print('Utilizando o forma de pagamento {}, sua compra terá o valor de {:.2f}R$'.format(d, valor))
else:
    print('Por favor escolha uma forma de pagamento correta.')