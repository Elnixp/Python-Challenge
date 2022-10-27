nome = input("Digite o nome da sua cidade: ").lower()
# busca = nome.find('Santo')
nome = nome.split()
if nome[0] == 'santo':
    #print(nome[0])
    print('A sua cidade começa com a palavra Santo')
else:
    print('Sua cidade não começa com a palavra "Santo"')