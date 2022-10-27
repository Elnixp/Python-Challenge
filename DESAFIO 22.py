nome = input('Digite seu nome completo:')
nome_split = nome.split()

print('Seu nome com todas as letras minúsculas: {}\n'
      'Seu nome com todas as letras maiúsculas: {}\n'
      'Seu nome tem {} caracteres sem contar espaços.\n'
      'Seu primeiro nome tem {} caracteres.'.format(nome.lower(), nome.upper(), len("".join(nome_split)), len(nome_split[0])))
