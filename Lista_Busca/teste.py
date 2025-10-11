
def buscaSequencial(lista, chave): 
    indice = 0
    for numero in lista:
        if numero == chave:
            return indice 
        indice = indice + 1
    return -1


lista = [1,2,3,4,5,6,7,8,9,10]
chave = int(input("insira uma chave: "))

resultado = buscaSequencial(lista, chave)
print(resultado)