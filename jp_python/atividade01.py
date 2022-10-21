nomes = {}

for contador in range(3):
    nome = input(f'Informe o {contador + 1}º nome: ')
    idade = int(input(f'Informe a {contador + 1}ª idade: '))
    nomes[nome] = idade
print(nomes)

for item in nomes.items():
    print(item)
for chave in nomes.keys():
    print(chave)
for valor in nomes.values():
    print(valor)

lista = []
print('Adcionar nomes na lista')
for chave, valor in nomes.items():
    if valor >= 18:
        lista.append(chave)
print(lista)

listaIdade = []
for idade in nomes.values():
    listaIdade.append(idade)
print(f'A soma das idades é {sum(listaIdade)} e a média é {sum(listaIdade)/len(listaIdade):.2f}')
print(f'A menor idade é {min(listaIdade)} e a maior idade é {max(listaIdade)}.')

