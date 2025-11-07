
"""
    Implementação do algoritmo Bubble Sort (Ordenação por Bolha).
    Repetidamente percorre o array, compara elementos adjacentes e troca
    se estiverem na ordem errada. O maior elemento 'sobe' como uma bolha.
    
    Vantagens:
    - Extremamente simples de implementar
    - Não requer memória extra (ordenação in-place)
    - Detecta automaticamente se o array já está ordenado (com otimização)
    - Bom para listas quase ordenadas ou muito pequenas
    
    Desvantagens:
    - Complexidade O(n²) no pior e médio caso
    - Muito lento para grandes conjuntos de dados
    - Número excessivo de trocas (até O(n²))
    - Não é eficiente mesmo com dados parcialmente ordenados sem otimização
"""


def bubble_sort(arr):

    n = len(arr) # armazena o tamanho do array

    for i in range(n - 1):
        trocou = False


        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]: # se o elemento atual for maior que o elemento da frente
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # troca suas posiçoes
                trocou = True

        # se nao houver trocas é porque a lista ja esta ordenada
        if not trocou:
            break

    return arr


dados = [64, 34, 25, 12, 22, 11, 90]
print("Antes:", dados)
bubble_sort(dados)
print("Depois:", dados)