import math
n = float(input('Digite o valor do ângulo?: '))
seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangente = math.tan(math.radians(n))
print('O seno do ângulo é {:.2f} \n'
      'O cosseno do ângulo é {:.2f} \n'
      'A tangente do ângulo é {:.2f}'.format(seno, cosseno, tangente))
