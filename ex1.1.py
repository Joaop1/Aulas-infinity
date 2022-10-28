def inteiro(numero):
    nInteiro = numero
    if nInteiro < 0:
        print(f'{nInteiro} é um número negativo!')
    elif nInteiro > 0:
        print(f'{nInteiro} é um número positivo!')
    else:
        print(f'O numero informado é {nInteiro}')

inteiro(0)
