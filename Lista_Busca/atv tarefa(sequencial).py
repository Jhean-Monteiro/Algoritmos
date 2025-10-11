# Tarefa 1 - Compare o tempo de execução e uso de memória para algoritmos de busca sequencial e binária. Para o teste considere uma lista de 1000 000 de elementos inteiros e randômicos.

import random
import time
import tracemalloc




tracemalloc.start()

start = time.time()


def buscaSequencial(lista, chave):
    for (indice, numero) in enumerate(lista): 
        if numero == chave:
            return indice
    return -1

lista = [random.randint(1,100) for i in range(1000000)]
chave = int(input("insira uma chave: "))

resultado = buscaSequencial(lista, chave)
print(resultado)


finish = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"o tempo de execução é: {finish-start:.3f} segundos")
print(f"memoria atual é: {memoria_atual/1024:.3f} KB")
print(f"pico memoria é: {memoria_pico/1024:.3f} KB")