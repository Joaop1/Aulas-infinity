def quantPares(numero1, numero2):
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        print('Números pares: 2')
    elif numero1 % 2 != 0 and numero2 % 2 != 0:
        print('Números pares: 0')
    else:
        print('Números pares: 1')
usuario1 = int(input('Informe o primeiro número: '))
usuario2 = int(input('Informe o segundo número: '))
quantPares(usuario1, usuario2)