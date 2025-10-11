import random
import time
import tracemalloc

# lista de randomica inteiros(0-9) com 1000 elementos.
tracemalloc.start()

start = time.time()


lista = [random.randint(1,100) for i in range(1000000)]
print(lista)
finish = time.time()

memoria_atual,memoria_pico = tracemalloc.get_traced_memory()

tracemalloc.stop()

print(f"o tempo de execução é: {finish-start:.3f} segundos")
print(f"memoria atual é: {memoria_atual/1024:.3f} KB")
print(f"pico memoria é: {memoria_pico/1024:.3f} KB")