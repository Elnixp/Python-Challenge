print('#################Cálculo de IMC################')
peso = float(input('Qual seu peso em Kg? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 35:
    print('Obesidade')
else:
    print('Obesidade mórbida')