from datetime import date
ano = int(input('Que ano você nasceu: '))
today = date.today()
alistar = today.year - ano

if alistar >= 18:
    print('já passou o tempo de alistamento')
elif 17 < alistar < 18:
    print('É a hora de se alistar')
elif alistar <= 17:
    print('você é muito novo')