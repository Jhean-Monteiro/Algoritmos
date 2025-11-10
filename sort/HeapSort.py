def HeapSort(lista):       # heap = arvore, pilha
    n = len(lista)                                         # Armazena o tamanho da lista na variável n

    # etapa 1: constroi um max-heap a apartir da lista 
    for i in range(n // 2 - 1, -1, - 1):                   # Loop do último nó não-folha (n//2 - 1) até a raiz (0), com passo -1
        heapify(lista, n, i)                               # Chama heapify para manter a propriedade de heap na subárvore

    for i in range(n - 1, 0, -1):                          # Loop do penúltimo índice (n-1) até o índice 1, com passo -1
        lista[0], lista[i] = lista[i], lista[0]            # Troca o maior elemento (raiz) com o último do heap
        heapify(lista, i, 0)                               # Reorganiza o heap reduzido (tamanho i) a partir da raiz

    return lista                                           # Retorna a lista ordenada


def heapify(lista, n, i):                                  # Função que garante a propriedade de Max-Heap a partir do nó i
    largest = i                                            # Assume que o nó atual (i) é o maior
    left = 2 * i + 1                                       # Calcula o índice do filho esquerdo
    right = 2 * i + 2                                      # Calcula o índice do filho direito

    if left < n and lista[left] > lista[largest]:          # Se o filho esquerdo existe e é maior que o atual maior
        largest = left                                     # Atualiza o índice do maior para o filho esquerdo

    if right < n and lista[right] > lista[largest]:        # Se o filho direito existe e é maior que o atual maior
        largest = right                                    # Atualiza o índice do maior para o filho direito

    if largest != i:                                       # Se o maior não for o nó original (houve troca)
        lista[i], lista[largest] = lista[largest], lista[i]# Troca o nó atual com o maior filho
        heapify(lista, n, largest)                         # Recursivamente aplica heapify na subárvore afetada


lista =  [64, 34, 25, 12, 22, 11, 90, 88, 45, 34, 25, 12, 22, 11, 90, 88, 45]  # Cria a lista de exemplo com duplicatas

lista_ordenada = HeapSort(lista.copy())                    # Chama HeapSort em uma cópia da lista original
print(lista_ordenada)                                      # Imprime a lista 



importante = [
"O Heap Sort coloca o maior elemento no final da lista, elimina esse índice do heap (não mexe mais nele), e repete com o novo maior, construindo a lista ordenada do final para o início."
              
"é mais eficiente que quicksort em ambiente com memoria limitada, tambem em lista quase ordenada ou ordenada"
              ]


vantagens = [
    "complexidade garantida O(n log n) em todos os casos",
    "algoritmo in-place (usa apenas O(1) de memoria extra)",
    "previsivel e nao depende do tipo de entrada",
    "excelente para filas de prioridade e algoritmos de grafos",
    "nao degrada com listas ordenadas ou com duplicatas"
]

desvantagens = [
    "vai muitas desnecessarias em alguns casos"
    "nao e estavel (elementos iguais podem trocar de ordem)",
    "mais complexo de entender e implementar",
    "versao recursiva pode estourar a pilha em listas muito grandes"
    "na maioria dos casos, quicksort e mais rapido, devido ao melhor uso de cache e menos overhead(sobrecarga)"
]