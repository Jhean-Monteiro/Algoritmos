def busca_binaria_iterativa(lista, alvo):
    pos_ini = 0 # indice inicial
    pos_fim = len(lista) - 1 # indice final

    while pos_ini <= pos_fim: # loop enquanto os indices não se cruzam
        meio = (pos_ini + pos_fim) // 2 # calcula o indice do meio (inteiro)

        if lista[meio] == alvo: # verifica se o elemento do meio é o alvo
            return meio # retorna o indice se encontrado
        
        elif lista[meio] < alvo: # se o elemento do meio for menor que o alvo
            pos_ini = meio + 1 # move a posicao inicial para depois do meio
            # print(pos_ini)
        elif lista[meio] > alvo:
            pos_fim = meio - 1 # move a posicao final para antes do meio
            # print(pos_fim)

    return - 1


lista_ord = []
for i in range(1,100):
    lista_ord.append(i) 

alvo = 20

resultado = busca_binaria_iterativa(lista_ord, alvo)
if resultado != -1:
    print(f"Elemento {alvo} encontrado no indice {resultado}")

else:
    print(f"Elemento {alvo} não encontrado na lista")