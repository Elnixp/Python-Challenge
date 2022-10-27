salario = float(input('Qual o seu sálario em Reais: '))
if salario > 1250:
    salario = salario*1.1
    print('O novo salário após o reajuste de 10% será de {:.2f}'.format(salario))
else:
    salario = salario*1.15
    print('O novo salário após o reajuste de 15% será de {:.2f}'.format(salario))
