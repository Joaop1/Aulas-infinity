'''Conceitos:
• Variáveis e tipos de dados
• Função Print
• Função Input
• Type
• Casting

• Operadores aritméticos (+, -, *, /, …)
• Como contamos as letras de uma string?

Estruturas Condicionais:
• Operadores relacionais (>, <, !=, ==, …)
• Tabela verdade (and, or)
• Condicional com if e else
• Condicional com if, elif e else

Estruras de repetição:
• Estruturas de repetição (while)
• Estruturas de repetição (for)'''

#• Variáveis e tipos de dados
nome = 'João Pedro'
idade = int(27)
altura = float(1.86)

#• Função Print
print(f"O {nome} tem {idade} anos e {altura} de altura")
#• Função Input
time = input("Informe qual time você torce: ")
#• Type
print(type(nome))
#• Casting
filhos = int(input("Você tem quantos filhos? "))
#• Operadores aritméticos (+, -, *, /, …)
soma = 2 + 2
print(soma)
subt = 5 - 2
print(subt)
mult = 7 * 9
print(mult)
div = 10 / 2
print(div)
div_int = 56 // 12
print(div_int)
potencia = 4 ** 3
print(potencia)
modulo = 4 % 2
print(modulo)
preced = 4 * (5+7)
print(preced)
#• Como contamos as letras de uma string?
print(len(nome))
'''• Operadores relacionais (>, <, !=, ==, …)
• Tabela verdade (and, or)
• Condicional com if e else
• Condicional com if, elif e else'''
if soma > subt and soma < div:
    print(f"O número {soma} é maior que {subt} e o número {soma} é menor que {div}")
elif modulo < preced or modulo < div_int:
    print(f"O número {modulo} é menor que {preced} ou o número {modulo} é menor que {div_int} ")
else:
    print(preced)
#• Estruturas de repetição (while)
i = 0
numero = int(input("Informe um número"))
while i <= numero:
    print(numero)
    i = i + 1



