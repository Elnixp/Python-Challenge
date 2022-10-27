n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
list = [n1, n2, n3]
list.sort()
print('O maior número é {} e o menor número é {}'.format(list[-1], list[0]))

