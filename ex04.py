"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    listIndice = lista[indice]
    typeIndice = type(lista[indice])
    print(indice, listIndice, typeIndice)