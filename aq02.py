lista = []
for i in range(5):
    idade = int(input(f'Informe a {i + 1}ª idade: '))
    lista.append(idade)

media = sum(lista) / len(lista)

if media <= 18:
    print('População jovem')
elif media <= 58:
    print('População adulta')
else:
    print('População idosa')

