vel = int(input('Digite sua velocidade: '))
if vel <= 60:
    print("Velocidade permitida!")
elif vel <= 80:
    print("Alta velocidade!")
elif vel <= 120:
    print("Muito rápido!")
else:
    print("Vuado!")