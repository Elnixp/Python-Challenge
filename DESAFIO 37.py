n = int(input('Digite um número inteiro qualquer: '))
print('Escolha qual será a base de conversão.\n'
      '1 para número binário;\n'
      '2 para octal;\n'
      '3 para hexadecimal.')
base = int(input('Qual a base de conversão?: '))
if base == 1:
      binario = bin(n)[2:]
      print('O número {}, na base binária é {}'.format(n, binario))
elif base == 2:
      octal = oct(n)[2:]
      print('O número {}, na base octal é {}.'.format(n, octal))
elif base == 3:
      hexadecimal = hex(n)[2:]
      print('O número {}, na base hexadecimal é {}.'.format(n, hexadecimal))
else:
      print('Por favor escolha uma base na nossa lista apresentada.')