nome = input('Digite seu nome completo: ')
nome_l = nome.split()
nome_r = nome.rsplit(' ')[-1]
print('Seu primeiro nome é {}\n'
      'Seu último nome é {}'.format(nome_l[0], nome_r))
