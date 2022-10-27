print('Programa para aprovação de empréstimo')
valor_casa = float(input('Qual o valor da casa? em Reais: '))
salario = float(input('Qual o seu Sálario? '))
tempo = int(input('quantos meses durará o empréstimo: '))
mensal = valor_casa/tempo
if mensal >= 0.3 * salario:
    print('Infelizmente seu empréstimo não pode ser aprovado,\n'
          'a prestação mensal excedeu 30% do seu sálario.\n'
          'o valor de {}R$ da prestação mensal excede 30% do seu sálario que corresponde a {}R$.'.format(mensal, 0.3*salario ))
else:
    print('Parabéns seu empréstimo foi aprovado com as condições:\n'
          '{:.2f}R$ o valor da casa\n'
          '{:.2f}R$ seu sálario\n'
          '{} meses é o tempo que irá durar o empréstimo\n'
          '{:.2f}R$ é o valor mensal que você deverá pagar.'.format(valor_casa, salario, tempo, mensal))

