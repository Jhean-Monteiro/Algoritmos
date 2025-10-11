# Tarefa 1 - Compare o tempo de execução e uso de memória para algoritmos de busca sequencial e binária. Para o teste considere uma lista de 1000 000 de elementos inteiros e randômicos.


import random
import time
import tracemalloc


tracemalloc.start()
start = time.time()


def buscaBinaria(lista, chave): 
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        elif lista[pos_meio] > chave: 
            pos_fim = pos_meio - 1
        elif lista[pos_meio] < chave: 
            pos_ini = pos_meio + 1
    return -1

lista = [random.randint(1,100000) for i in range(100000)]
lista.sort()
print(lista)
chave = int(input("insira uma chave: "))

resultado = buscaBinaria(lista, chave)
print(resultado)


finish = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"o tempo de execução é: {finish-start:.3f} segundos")
print(f"memoria atual é: {memoria_atual/1024:.3f} KB")
print(f"pico memoria é: {memoria_pico/1024:.3f} KB")