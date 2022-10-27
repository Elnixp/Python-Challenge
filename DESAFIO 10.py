n = float(input("Quantos reais você tem? R$:"))
c = n//5.21
resto_c = n%5.21
if (c==0):
    print('Você é pobre, fique com seus miseros {} reais.'.format(resto_c))
if (c==1):
    print('Você só pode comprar 1 Dolár e ainda restará miseros {:.2f} reais.'.format(resto_c))
elif (c>1):
    print('Você pode comprar {} dólares e ainda restará miseros {:.2f} reais.'.format(c, resto_c))

