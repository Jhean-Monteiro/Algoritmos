def buscaSequencial(lista, chave):
    for (indice, numero) in enumerate(lista): 
        if numero == chave:
            return indice
    return -1

lista = [1,2,3,4,5,6,7,8,9,10]
chave = int(input("insira uma chave: "))

resultado = buscaSequencial(lista, chave)
print(resultado)