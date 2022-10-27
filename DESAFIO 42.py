print('Quer saber se três medidas podem formar um triangulo?')
a = float(input('Digite o lado a: '))
b = float(input('Digite o lado b: '))
c = float(input('Digite o lado c: '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b and a == b and a == c:
    print('Os valores {}, {}, {} podem formar um triângulo'.format(a, b, c))
    print('Seu triangulo é Equilátero')
elif abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b and a == b or b == c or a == c:
        print('Os valores {}, {}, {} podem formar um triângulo'.format(a, b, c))
        print('Seu triangulo é Isósceles ')
elif abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b and a != b and b != c:
        print('Os valores {}, {}, {} podem formar um triângulo'.format(a, b, c))
        print('Seu triangulo é Escaleno')
else:
    print('Os valores não podem formar um triângulo')