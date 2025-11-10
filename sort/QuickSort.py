import time
import tracemalloc

tracemalloc.start()

start = time.time()


def quick_sort(lista):
    # caso base: se a lista tiver 0 ou 1 elemento, ja esta ordenada
    if len(lista) <= 1: # 
        return lista
    
    # escolhe o pivo (aqui usamos o ultimo elemento como pivo)
    pivot = lista[-1]

    # listas auxiliares para elementos maiores, iguais e maiores que o pivo
    left = [] # elementos menores q o pivo
    middle = [] # elementos iguais ao pivo
    right = [] # elementos maiores que o pivo

    #  percorre todos os elementos da lista
    for item in lista:
        if item < pivot:
            left.append(item) # adiciona à esquerda se for menor

        elif item == pivot:
            middle.append(item) # adiciona ao meio se for igual


        else:
            right.append(item) # adiciona à direita se for maior

    # recursao: ordena as sublistas esquerda e direita
    # e concatena: (ordenada esquerda) + (meio) + (ordenada direita)
    return quick_sort(left) + middle + quick_sort(right)

lista = [64, 34, 25, 12, 22, 11, 90, 88, 45]
# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,9999999999999, 100000000000000]

listaOrdenada = quick_sort(lista)
print(listaOrdenada)



finish = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"o tempo de execução é: {finish-start:.9f} segundos")
print(f"memoria atual é: {memoria_atual/1024:.9f} KB")
print(f"pico memoria é: {memoria_pico/1024:.9f} KB")


vantagens = [
    "bom desempenho com cache (aproveita bem a cache da cpu)"
    "funciona bem com muitos duplicados"
    "bom com listas randomicas"
    "usado no sorted() do python"
]

desvantagens = [
    "elementos iguais podem trocar de ordem"
    "pivo mal escolhido degrada o desempenho"
    "as listas auxiliares (left, middle, e right) consomem memoria extra"
    "se a lista for ordenada, a recursao fica desbalanceada"
]







# Exemplo BOM (Quick Sort brilha)
ExemploBom = [64, 34, 25, 12, 22, 11, 90, 88, 45, 3, 56, 78, 19]
# n = 13, elementos "aleatórios"

# Distribuição: Valores bem misturados, sem padrão.
# Pivô: Escolhido como o último (ou mediana, ou aleatório).
# Particionamento: Divide a lista em metades quase iguais a cada passo.

# Complexidade real: O(n log n) → muito rápido!

# Quick Sort é um dos mais rápidos na prática para dados aleatórios.




# Exemplo RUIM (Quick Sort vira pesadelo)
ExemploRuim = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # n = 10
# Já ordenada (ou quase ordenada)

# Pivô: Se escolher o último elemento (10), o particionamento fica desbalanceado:
# Esquerda: [1,2,3,4,5,6,7,8,9] (9 elementos)
# Direita: [] (vazio)

# A cada chamada, remove apenas 1 elemento.
# Total de chamadas: n → pior caso!

# Complexidade: O(n²) → lento como um bubble sort!