contador = 1
soma = 0
while True:

    nota = float(input(f"Informe a {contador}ª nota: "))
    if nota < 0:
        print("Esta é inválida, tente novamente!")
    else:
        soma = soma + nota
        pergunta = int(input("Deseja continuar?\n[1] SIM\n[2] NÃO\n"))
        if pergunta == 1:
            contador = contador + 1
        else:
            break

media = soma / contador
print(f"A média é {media}.")