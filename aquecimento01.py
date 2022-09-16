nome1 = input("Informe um nome: ")
nome2 = input("Informe outro nome: ")

if len(nome1) > len(nome2):
    print(f"{nome1} é maior do que {nome2}")
elif len(nome2) > len(nome1):
    print(f"{nome2} é maior do que o nome {nome1}")
else:
    print(f"O s dois nomes tem {len(nome1)} letras")
