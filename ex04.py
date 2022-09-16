
n1 = int(input("Limite inferior: "))
n2 = int(input("Limite superior: "))
totalPares = 0
for contador in range(n1,n2+1):
    if contador % 2 == 0:
        totalPares = totalPares + 1
print(f"O total de números PARES entre {n1} e {n2} é {totalPares}")