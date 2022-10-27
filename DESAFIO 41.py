from datetime import date
ano = int(input('Qual o ano de seu nascimento: '))
today = date.today()
idade = today.year - ano
if idade > 20:
    print('Sua categoria é Master')
elif 19 <= idade < 20:
    print('Sua catogoria é Sênior')
elif 14 <= idade < 19:
    print('Sua categoria é Junior')
elif 9 <= idade < 14:
    print('Sua categoria é Infantil')
elif 0 <= idade < 9:
    print('Sua categoria é Mirin')
elif idade <= 0:
    print('Por favor insira uma data de nascimento válida')