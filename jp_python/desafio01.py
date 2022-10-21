nomes01 = {}

for i in range(4):
    nome = input(f'Digite o nome o {i + 1}º aluno: ')
    matricula = input(f'Digite a {i+1}ª matrícula: ')
    nomes01[nome] = matricula
print(nomes01)

backup = nomes01.copy()
print(nomes01.copy())

nomes01.clear()
print(nomes01)

for i in range(4):
    nome = input(f'Digite o nome o {i + 1}º aluno: ')
    matricula = input(f'Digite a {i+1}ª matrícula: ')
    nomes01[nome] = matricula

print(nomes01)
print(backup)
