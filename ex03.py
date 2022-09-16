soma = 0
for i in range(1,6):
    numero = int(input(f"Digite o {i}º número: "))
    soma = soma + numero

media = soma / i
print(f"A soma é {soma} e a média é {media}")
