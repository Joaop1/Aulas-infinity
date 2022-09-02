peso = float(input("Digite o seu peso: "))
alt = float(input("Digite sua altura: "))
imc = peso / (alt**2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('sobrepeso')
elif imc <= 39.9:
    print('Obesidade tipo I')
else:
    print('Alerta: Obesidade mórbida')