import time
import tracemalloc

tracemalloc.start()

start = time.time()



def counting_sort(lista):
    if not lista:
        return lista
    
    # passo 1: Encontrar o maior valor
    max_val = max(lista)

    # passo 2: Criar array de contagem (inicializado com zeros)
    count = [0] * (max_val + 1)

    # passo 3: contar ocorrencias
    for num in lista:
        count[num] += 1

    sorted_lista = []
    for i in range(len(count)):
        sorted_lista.extend([i] * count[i])

    return sorted_lista



lista = [4000, 2, 2, 8, 3, 3, 1]
ord = counting_sort(lista)
print(ord)

importante = [
     "O Counting Sort é ótimo principalmente quando os elementos da lista estão próximos uns dos outros, ou seja, quando o intervalo entre o menor e o maior valor é pequeno em relação ao tamanho da lista."

     "O Count Sort nao compara elementos, ele conta quantas vezes cada valor aparece"

     "A eficiência depende do tamanho do intervalo, não do número de elementos."
]



"Exemplo bom (Counting Sort brilha)"
exemplo_ruim = [5, 1, 4, 2, 8, 3, 1, 5, 2]  # n = 9
# min = 1, max = 8 → intervalo = 8

n = 9
k = 8 # (maior valor)
# Complexidade: O(n + k) = O(17) → muito rápido!



"exemplo ruim"
exemplo_ruim = [1, 1000000, 500000, 2] # n = 4
# min = 1, max = 1.000.000 --> intervalo = 999.999

n = 4
k = 1.000,000
# complexidade: 0(1.000.004) --> desperdicio de memoria e de tempo

# mesmo com so 4 elementos, usa 1 milhao de array de contagem




finish = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"o tempo de execução é: {finish-start:.9f} segundos")
print(f"memoria atual é: {memoria_atual/1024:.9f} KB")
print(f"pico memoria é: {memoria_pico/1024:.9f} KB")