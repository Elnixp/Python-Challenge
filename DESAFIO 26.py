txt = input('Digite um texto: ').lower().strip()
txt_l = (txt.find('a')+1)
txt_r = (txt.rfind('a')+1)
txt_count = txt.count('a')
print('A letra "a", aparece {0} vezes no texto que vc digitou\n'
      'a posição inicial que a letra "a" aparece é {1}\n'
      'a posição final que a letra "a" aparece é {2}'.format(txt_count, txt_l, txt_r))
