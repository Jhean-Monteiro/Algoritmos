'''
Estudo de Caso 2 – Lista de compras interativa
Enunciado:
Faça um programa que:
1. Permita ao usuário adicionar itens a uma lista de compras.
2. Caso o usuário digite "sair", o programa encerra.
3. Mostre a lista final de compras organizada em ordem alfabética.
'''

compras = [] # cria uma lista vazia para armazenar os itens de compra
total = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27] # limite de compras
i = 0 # contador

print(f'olá! nesse sistema voce pode anotar sua lista de compras! escreva o nome das compras que voce quer adicionar.')

while i < len(total): # enquanto o contador for menor que o tamanho da lista total
    compra = input(f'adicione um novo iten {i+1}: ')
    item = compra # armazena a entrada do usuário na variavel item
    compras.append(compra) # adiciona o item digitado pelo usuário à lista de compras
    if compra in ['sair']: # se o usuário digitar 'sair'...
        break # cancela o loop se 'sair for digitado
    i += 1 # aumenta o contador

compras.pop(-1) # remove o ultimo item 'sair' da lista
print('lista de compras:', compras)