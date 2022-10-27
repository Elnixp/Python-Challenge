nota1 = float(input('Qual a primeira nota?: '))
nota2 = float(input('Qual a segunda nota?: '))
media = (nota1 + nota2)/2
if media > 7:
    print('Aprovado sua média foi {:.2f}'.format(media))
elif 5 <= media < 7:
    print('Recuperação sua média foi {:.2f}'.format(media))
else:
    print('Reprovado sua média foi {:.2f}'.format(media))
