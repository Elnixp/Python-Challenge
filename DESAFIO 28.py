from random import randint
from time import sleep
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
pc = randint(0, 5)
print('-=-' * 18)
jogador = int(input('Qual número eu pensei?...'))
print('PROCESSANDO.')
sleep(1)
print('PROCESSANDO..')
sleep(2)
print('PROCESSANDO...')
sleep(3)
if jogador == pc:
    print('Acertou mizeravi!')
else:
    print('Cuen cuen cuen cuen, eu pensei no número {} e não no {} seu lixo'.format(pc, jogador))