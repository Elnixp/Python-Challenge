p = float(input('Qual o preço do produto?'))
novo_p = p*0.95
desconto = p - novo_p
print('Na liquidação o novo valor fica {:=5} reais, totalizando um desconto de {:=.3} reais'.format(novo_p, desconto))
