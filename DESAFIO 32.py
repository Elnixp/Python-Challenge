ano = int(input('Digite o ano para saber se ele é bissexto ou não: '))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 ==0:
    print('O ano é bissexto')
elif ano % 4 == 0 and ano % 100 != 0:
    print('O ano é bissexto')
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 !=0:
    print('O ano não é bissexto')
elif ano % 4 != 0:
    print('O ano não é bissexto')