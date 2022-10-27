n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor digitado é maior pois {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor digitado é maior pois {} é maior que {}'.format(n2, n1))
else:
    print('O dois valores são iguais')