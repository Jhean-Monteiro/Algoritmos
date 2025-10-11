def buscaBinaria(lista, chave): 
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        elif lista[pos_meio] > chave: 
            pos_fim = pos_meio - 1
        elif lista[pos_meio] < chave: 
            pos_ini = pos_meio + 1
    return -1

lista = [1, 40, 2,3,4,5,6,7,8,9,10]
lista.sort()
chave = int(input("insira uma chave: "))

resultado = buscaBinaria(lista, chave)
print(resultado)