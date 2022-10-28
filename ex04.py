def intPorcent(num1, num2):
    soma = num1 + (num1*(num2/100))
    return soma
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = intPorcent(num1, num2)
print(soma)