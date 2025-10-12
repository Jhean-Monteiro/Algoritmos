import random # modulo random para gerar numeros aleatorios
import time
import tracemalloc # modulo tracemalloc para medir o uso de memória

tracemalloc.start() # inicia a medição ddo uso de memória
start = time.time() # registra o tempo inicial para medir a duração do programa

lista = [random.randint(1,100000) for i in range(1000000)] # gera lista com 1M de intteiros aleatorios (1 a 100000)
lista_ordenada = sorted(lista)
chave = int(input("Insira uma chave: "))




# Busca Linear Simples 
# Dado um vetor de números inteiros e um número alvo, use busca sequencial para 
# verificar se o número está presente. 
# Extra: informe o índice se encontrar. 

def buscaSequencial(lista, chave):
    for indice, numero in enumerate(lista): # (para cada indice e valor dentro da lista:)
        if numero == chave:
            return indice
    return -1


# lista = [random.randint(1,100000) for i in range(1000000)] # gera lista com 1M de intteiros aleatorios (1 a 100000)
# lista_ordenada = sorted(lista)
# chave = int(input("Insira uma chave: "))

resultado_busca_sec = buscaSequencial(lista, chave)
print(f"Busca Sequencial: Chave {chave} {'encontrada no índice ' + str (resultado_busca_sec) if resultado_busca_sec != -1 else 'não encontrada'}")



# -------------------------------------------------------------------------------------------------------------------------------------------------------



# Contar Ocorrências (Busca Linear) 
# Conte quantas vezes um número aparece na lista usando busca sequencial.

def contarOcorrencias(lista,chave):
    contagem = 0
    for numero in lista:
        if numero == chave:
            contagem += 1
    return contagem
    
ocorrencias = contarOcorrencias(lista,chave)
print(f"Contagem de Ocorrencias: A Chave: {chave} aparece {ocorrencias} vezes")



# -----------------------------------------------------------------------------------------



# 3. Maior Número (Busca Linear) 
# Use busca sequencial para encontrar o maior número em uma lista.

def maiorNumero(lista):
    if not lista: # verifica se a lista está vazia
        return None
    maior = lista[0] # inicializa o maior numero com o primeiro elemento
    for numero in lista:
        if numero > maior: # verifica se o número atual é maior que o atual maior
            maior = numero # atualiza o maior numero se necessário
    return maior

maior = maiorNumero(lista)
print(f"Maior Número: {maior}")



#------------------------------------------------------------------------------------------------------



# 4. Menor Número (Busca Linear) 
# Similar ao anterior, mas encontre o menor valor. 

def menorNumero(lista):
    if not lista: # verifica se a lista está vazia
        return None
    menor = lista[100000] # inicializa o menor numero com o maior elemento
    for numero in lista:
        if numero < menor: # verifica se o número atual é menor que o atual menor
            menor = numero # atualiza o menor numero se necessário
    return menor

menor = menorNumero(lista)
print(f"Menor Número: {menor}")



#---------------------------------------------------------------------------------------------



# 5. Verificar Elemento (Busca Binária) 
# Dada uma lista ordenada, implemente a busca binária para verificar se o 
# elemento existe. 

def buscaBinaria(lista,chave):
    pos_ini = 0 # define o indice inicial como 0
    pos_fim = len(lista)-1 # define o índice final como o último indice da lista

    while pos_ini <= pos_fim: # continua enquanto o indice inicial for menor ou igual ao final
        pos_meio = (pos_ini + pos_fim) // 2 # calcula o indice do meio (divisão inteira)
        if lista[pos_meio] == chave: # verifica se o elemento do meio é a chave
            return pos_meio # retorna o índice do meio se a chave for encontrada
        
        elif lista[pos_meio] > chave:
            pos_fim = pos_meio - 1 # ajusta o indice final para buscar na metade inferior
        
        else:
            pos_ini = pos_meio + 1
    return -1

resultado_busca_bin = buscaBinaria(lista_ordenada,chave) # busca binária só funciona com lista ordenada
print(f"Busca Binária: Chave {chave} {'encontrada no índice ' + str (resultado_busca_bin) if resultado_busca_bin != -1 else 'não encontrada'}")






finish = time.time()  # Registra o tempo final
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()  # Obtém memória atual e pico
tracemalloc.stop()  # Para a medição de memória

print(f"\nTempo de execução: {finish - start:.3f} segundos")  # Exibe o tempo total de execução
print(f"Memória atual: {memoria_atual / 1024:.3f} KB")  # Exibe a memória atual em KB
print(f"Pico de memória: {memoria_pico / 1024:.3f} KB")  # Exibe o pico de memória em KB