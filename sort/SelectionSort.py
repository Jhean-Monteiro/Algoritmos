# Algoritmo in-place (no lugar): [nao cria uma nova lista]

"Em cada passada, ache o menor elemento que ainda não está no lugar certo e jogue ele para a frente (troque com o primeiro da parte não ordenada)."

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

import time

def selection_sort(lista): 
    n = len(lista) 

    for j in range(n - 1):  # percorre ate o penultimo elemento
        print(lista[j])

        indice_menor = j  
        for i in range(j+1, n):  
            if lista[i] < lista[indice_menor]:  
                indice_menor = i
                print(lista)
                time.sleep(2)

        if lista[j] > lista[indice_menor]:
            aux = lista[j]
            lista[j] = lista[indice_menor]
            lista[indice_menor] = aux 

    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
print("antes:", lista)
selection_sort(lista)
print("depois", lista)