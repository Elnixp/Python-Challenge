# import math
# a = float(input('Digite o cateto oposto: '))
#b = float(input('Agora digite o cateto adjacente: '))
#c = math.sqrt(a**2 + b**2)
#print('Com o cateto oposto com valor {}, cateto adjacente valor {} a hipotenusa é {}'.format(a, b , c))

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Agora digite o cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa é {}'.format(hi))