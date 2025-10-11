def buscaSequencial(lista, chave): 
    n = len(lista)
    for indice in range(n):
        if lista[indice] == chave:
         return indice
    return -1
    
lista = [1,2,3,4,5,6,7,8,9,10]
chave = int(input("insira uma chave: "))

resultado = buscaSequencial(lista, chave)
print(resultado)


for i in range(len(lista)):
   print(i, lista[i])


for indice,elemento in enumerate(lista):
   print("\n\n\n",indice,elemento)