print("-"*50)
print("INICIANDO O CÓDIGO")
print("-"*50)
print()

def pedirPares():
    par01 = int(input("Digite o primeiro par: "))
    par02 = int(input("Digite o SEGUNDO par: "))
    if par01 > par02:
        return par01
    elif par02 > par01:
        return par02
    else:
        return par01

def pedirImpares():
    impar01 = int(input("Digite o PRIMEIRO ímpar: "))
    impar02 = int(input("Digite o SEGUNDO ímpar: "))
    if impar01 > impar02:
        return impar01
    elif impar02 > impar01:
        return impar02
    else:
        return impar01

maiorPar = pedirPares()
maiorImpar = pedirImpares()
soma = maiorPar + maiorImpar

print(f"A soma do maior par e do maior ímpar é {soma}.")


