import time
import tracemalloc

tracemalloc.start()

start = time.time()



def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0

    for k in range(inicio, fim):
        # CORREÇÃO 1: usar ELIF no segundo if (era if + if → executava os dois!)
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):  # ← mudou de "if" para "elif"
            lista[k] = left[top_left]
            top_left += 1
        # CORREÇÃO 2: agora o else está alinhado com o elif acima
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else: 
            lista[k] = right[top_right]
            top_right += 1

# ==========================
# TESTE
# ==========================
lista = [1, 2, 8, 7, 4, 6, 8, 9, 98, 76, 65, 4]
print("Antes:", lista)

merge_sort(lista)

print("Depois:", lista)


finish = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"o tempo de execução é: {finish-start:.9f} segundos")
print(f"memoria atual é: {memoria_atual/1024:.9f} KB")
print(f"pico memoria é: {memoria_pico/1024:.9f} KB")


# nao tem pior caso!!!

importante = ["Dizer que o Merge Sort não tem pior caso significa: nunca vai ficar lento e nunca vai estourar memória, não importa a entrada. Já o Counting Sort pode 'quebrar' completamente — se o intervalo for grande, não roda de jeito nenhum. Ou seja: Merge Sort é seguro. Counting Sort é uma bomba-relógio."]



"O Merge Sort em Python tem como vantagens sua complexidade de tempo garantida (\(O(n\log n)\)) e estabilidade, tornando-o eficiente para grandes conjuntos de dados e útil quando a ordem original de elementos iguais precisa ser preservada. As desvantagens incluem o uso de memória extra para sub-listas temporárias e, em geral, um desempenho um pouco mais lento em comparação com o Quick Sort na prática, embora isso possa variar dependendo do caso de uso. "

# estouro de pilha acontece quando a lista e muito grande. Mas não é o tamanho da lista em si, e sim a profundidade da recursão.

"""Sim, estouro de pilha acontece com listas muito grandes —porque a recursão cria muitas chamadas empilhadas. Em Python, o limite padrão é ~1000 chamadas.
Se a lista tiver mais de ~1.000.000 elementos,
Merge Sort, Heap Sort ou Quick Sort recursivo podem travar."""

# recursao: limite padrao: 1000 chamadas




"Merge"  "mesclar / juntar / intercalar"
"Sort"  "ordenar"
"Ordenação por juncao"
"""
Lista: [38, 27, 43, 3, 9, 82, 10]

1. Divide:
[38, 27, 43]     [3, 9, 82, 10]

2. Divide mais:
[38] [27] [43]   [3] [9] [82] [10]

3. Ordena e mescla (merge):
[27, 38, 43]     [3, 9, 10, 82]

4. Mescla final:
[3, 9, 10, 27, 38, 43, 82]
"""
Mesclagem = ["juntar duas listas ordenadas em uma só, comparando elemento por elemento."] 