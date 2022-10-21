titulo = 'O poder do hábito'
autor = 'Charles Duhigg'
data = '24.09.2012'
edicao = '1ª edição'
editora = 'Objetiva'
isbn = 8539004119

dicionario = {'Título': titulo, 'Autor': autor, 'Data': data, 'Edição': edicao, 'Editora': editora, 'ISBN': isbn}

print(type(dicionario))
print(dicionario)

print('Imprimindo os itens')
for item in dicionario.items():
    print(item)
print('Imprimindo a chave')
for chave in dicionario.keys():
    print(chave)
print('Imprimindo os valores')
for valor in dicionario.values():
    print(valor)