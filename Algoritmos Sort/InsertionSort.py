import random
lista = []
for i in range(20000):
   elemento = random.randint(1,20000)
   lista.append(elemento)

print(lista)


"""
    Implementação do algoritmo Insertion Sort (Ordenação por Inserção).
    Constrói a lista ordenada um elemento por vez, inserindo cada novo
    elemento na posição correta dentro da parte já ordenada.
    
    Vantagens:
    - Simples e intuitivo
    - Eficiente para listas pequenas ou quase ordenadas (O(n) no melhor caso)
    - Ordenação in-place (não precisa de memória extra)
    - Estável: mantém a ordem relativa de elementos iguais
    - Adaptativo: quanto mais ordenado, mais rápido
    
    Desvantagens:
    - Complexidade O(n²) no pior e médio caso
    - Muitas trocas/deslocamentos em listas grandes e desordenadas
    - Ineficiente para grandes conjuntos de dados aleatórios
"""


def insertion_sort(arr):
   n = len(arr)

   for i in range(1, n):
      chave = arr[i]
      j = i - 1

      while j >= 0 and arr[j] > chave:
         arr[j+1] = arr[j]
         j -= 1

      arr[j + 1] = chave


print("Antes:", lista)                 
insertion_sort(lista)               
print("Depois:", lista)
