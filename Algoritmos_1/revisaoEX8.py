# 4. Busca Linear 
# Dada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário. 
# Informe a posição em que ele aparece ou diga que não foi encontrado.

def busca_linear(lista,alvo):
    for i in range(len(lista)):
        if lista[i].lower()== alvo.lower():
            return i + 1
    return -1

nomes = ['Gioliano', 'João', 'Sergio', 'Andre', 'Diego',]
nome_buscar = input('escreva o nome a ser buscado: ')

posicao = busca_linear(nomes, nome_buscar)

if posicao != -1:
    print(f"nome '{nome_buscar}' encontrado na posição {posicao}")

else:
    print(f"nome '{nome_buscar} não foi encontrado'")