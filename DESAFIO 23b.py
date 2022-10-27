num = input('Digite um número: ')
if len(num) > 4:
    print('O número digitado é muito grande')
elif len(num) == 1:
    print('O número tem {} unidades'.format(num))
elif len(num) == 2:
    print('O número tem {} unidades\n'
          'O número tem {} dezenas'.format(num[1], num[0]))
elif len(num) == 3:
    print('O número tem {} unidades\n'
          'O número tem {} dezenas\n'
          'O número tem {} centenas'.format(num[2], num[1], num[0]))
elif len(num) == 4:
    print('O número tem {} unidades\n'
          'O número tem {} dezenas\n'
          'O número tem {} centenas\n'
          'O número tem {} milhar'.format(num[3], num[2], num[1], num[0]))