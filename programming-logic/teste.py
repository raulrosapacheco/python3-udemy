"""
Split: dividir string
Join: juntar uma lista (str)
Enumerate: enumerar elementos da lista (iteráveis)
"""
string ='O Brasil é o pais do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')
print(lista_1)
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')

    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes