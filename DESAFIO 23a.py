num = int(input('Digite um número inteiro entre 0 e 9999: '))
if num <= 9:
    print('O número tem {} unidades'.format(num))
elif 10 <= num <= 99:
    unidade = num%10
    dezena = int(((num - unidade)/10))
    print('O número tem {} unidades\n'
          'O número tem {} dezenas'.format(unidade, dezena))
elif 100 <= num <999:
    unidade = num%10
    dezena = int((num - unidade)%100)/10
    centena = int(num - dezena*10 - unidade)/100
    print('O número tem {} unidade\n'
          'O número tem {} dezenas\n'
          'O número tem {} centenas'.format(unidade, dezena, centena))
elif 1000 <= num <=9999:
    unidade = num%10
    dezena = int((num - unidade)%100)/10
    centena = int((num - dezena*10 - unidade)%1000)/100
    milhar = int(num - centena*100 - dezena*10 - unidade)/1000
    print('O número tem {} unidades\n'
          'O número tem {} dezenas\n'
          'O número tem {} centenas\n'
          'O número tem {} milhar'.format(unidade, dezena, centena, milhar))
elif num > 9999:
    print('O número digitado era muito grande')
