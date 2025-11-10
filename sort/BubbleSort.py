
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
    n = len(arr) 

    for i in range(n - 1):

        for j in range(n - 1):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)

    return arr

dados = [64, 34, 25, 12, 22, 11, 90]
print("Antes:", dados)
bubble_sort(dados)
print("Depois:", dados)