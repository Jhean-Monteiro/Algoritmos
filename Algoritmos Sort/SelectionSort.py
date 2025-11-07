"""
    Implementação do algoritmo Selection Sort (Ordenação por Seleção).
    Percorre o array, encontra o menor elemento na parte não ordenada
    e o coloca na posição correta.
    
    Vantagens:
    - Simples de implementar e entender
    - Não requer memória extra (ordenação in-place)
    - Bom para listas pequenas ou quando a escrita em memória é cara
    - Número fixo de trocas (O(n)), útil se trocas forem custosas
    
    Desvantagens:
    - Complexidade O(n²) mesmo no melhor caso
    - Não é estável (elementos iguais podem trocar de ordem)
    - Ineficiente para grandes conjuntos de dados
    - Não é adaptativo (não aproveita ordenação parcial existente)
"""

def selection_sort(arr):  # ordenacao por selecao
    n = len(arr)  # armazeena o tamanho do array em n

    # percorre todos os elementos exceto o ultimo
    for i in range(n - 1):  # i é o indice da posiçao atual a ser preenchido

        # assume que o menor elemento esta na posiçao i
        indice_menor = i  # inicializa o indice do menor valor

        # procura o menor elemento na parte nao ordenada (de i+1 até o final)
        for j in range(i + 1, n):  # j percorre o subarray nao ordenado
            if arr[j] < arr[indice_menor]:  # se encontrar um valor menor
                indice_menor = j # atualiza o indice menor

        # troca o menor elemento encontrado com o elemento na posiçao i
        if indice_menor != i: # so troca se for necessario (evita troca desnecessaria)
            arr[i], arr[indice_menor] = arr[indice_menor], arr[i]  # troca usando desempacotamento python


    return arr


lista = [64, 34, 25, 12, 22, 11, 90]
print("antes:", lista)
selection_sort(lista)
print("depois", lista)