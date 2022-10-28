'''AQUECIMENTO :
Utilizando o módulo TIME, crie, utilizando FOR e depois WHILE,
uma contagem regressiva e ao final, mostre a mensagem: FELIZ ANO NOVO!'''

import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print('Feliz ano novo!')

print('-'*5)
contador = 10
while contador > 0:
    print(contador)
    time.sleep(1)
    contador -= 1
print('Feliz ano novo!')