# Algoritmo in-place (no lugar): [nao cria uma nova lista]

import random
import time
lista = []
for i in range(9):
   elemento = random.randint(1,9)
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


def insertion_sort(lista):
   n = len(lista)
   contagem = 0

   for i in range(1, n):
      chave = lista[i]
      j = i - 1

      while j >= 0 and lista[j] > chave:
         lista[j+1] = lista[j]
         j = j - 1 
         print(f"lista{contagem+1}:", lista)
         time.sleep(2)
         contagem+=1

      lista[j + 1] = chave


print("Antes:", lista)                 
insertion_sort(lista)               
print("Depois:", lista)



"funcionamento na pratica: "

"""
vai comecar pelo segundo elemento da lista, e compara com o primeiro. 
se for maior que o primeiro, muda de lugar.
ininsere o numero em sua posicao ordenada
"""