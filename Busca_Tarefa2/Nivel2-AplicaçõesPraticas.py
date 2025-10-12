import random
import time
import tracemalloc

# nesse trecho é onde começa a ser executada a atv 8
tracemalloc.start()
start = time.time()

lista = [random.randint(1,50000) for i in range(100000)]



#----------------------------------------------------------------------



# 6. Busca de Nome em Lista 
# Peça ao usuário para digitar nomes e depois procure um nome específico usando 
# busca linear. 

def buscaNome(lista_nomes, nome):
    for indice, valor in enumerate(lista_nomes):
        if valor.lower() == nome.lower():
            return indice
    return - 1

print("Digite nomes (pressione Enter sem texto para encerrar): ")
nomes = []
while True:
    nome = input("Digite um nome: ")
    if nome == "":
        break
    nomes.append(nome)

nome_busca = input("Digite o nome a ser buscado: ")
resultado_nome = buscaNome(nomes,nome_busca)

print(f"Busca de Nome: Nome '{nome_busca}' {'encontrado no indice ' + str(resultado_nome) if resultado_nome != -1 else 'não encontrado'}")



#--------------------------------------------------------------------------------------------------------------------------------------------



# 7. Busca Binária Recursiva 
# Implemente a versão recursiva da busca binária em uma lista ordenada.

def buscaBinariaRecursiva(lista, chave): 
    lista.sort()
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

    
chave = int(input("insira uma chave: "))
resultado = buscaBinariaRecursiva(lista, chave)
print(f"Busca Binária Recursiva: Chave {chave} {'encontrada no índice ' + str(resultado)}")



#--------------------------------------------------------------------------------------------------------------------



# 9. Encontrar Primeira Ocorrência (Busca Binária Modificada) 
# Dada uma lista ordenada com elementos repetidos, use busca binária modificada 
# para encontrar o índice da primeira ocorrência de um número. 

def buscaPrimeiraOcorrencia(lista, chave):
    lista.sort()
    pos_ini = 0
    pos_fim = len(lista) - 1
    resultado = -1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            resultado = pos_meio
            pos_fim = pos_meio - 1
        elif lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return resultado

chave = int(input("Insira uma chave: "))

resultado = buscaPrimeiraOcorrencia(lista,chave)
if resultado != - 1:
    print(f"A primeira ocorrência da chave {chave} está no indice {resultado}")
else:
    print(f"A chave {chave} não foi encontrada na lista")



#---------------------------------------------------------------------------------------------------------------------------------



# 10. Localizar Intervalo de Índices 
# • Encontre o intervalo (início e fim) de um número que aparece mais de uma vez usando 
# busca binária (ex: [1,2,2,2,3,4] > número 2 > índices 1 a 3).

'''busca binária modificada para encontrar a primeira ocorrencia:'''
def buscaPrimeiraOcorrencia(lista, chave):
    lista.sort()
    pos_ini = 0
    pos_fim = len(lista) - 1
    resultado = - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            resultado = pos_meio
            pos_fim = pos_meio - 1 # continua buscando à esquerda
        elif lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return resultado

'''busca binária modificada para encontrar a ultima ocorrencia:'''
def buscaUltimaOcorrencia(lista, chave):
    lista.sort()
    pos_ini = 0
    pos_fim = len(lista) -1
    resultado = -1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            resultado = pos_meio
            pos_ini = pos_meio + 1
        elif lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return resultado


'''Função para encontrar o intervalo de índices'''
def localizarIntervalo(lista, chave):
    lista.sort()
    inicio = buscaPrimeiraOcorrencia(lista, chave)
    fim = buscaUltimaOcorrencia(lista, chave)
    return (inicio, fim)

chave = int(input("escreva uma chave: "))

inicio, fim = localizarIntervalo(lista, chave)
if inicio != -1 and fim != -1:
    print(f"O numero {chave} aparece no intervalo de indices {inicio} a {fim}")
else:
    print(f"o numero {chave} não foi encontrado na lista.")




finish = time.time()  # Registra o tempo final
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()  # Obtém memória atual e pico
tracemalloc.stop()  # Para a medição de memória

print(f"\nTempo de execução: {finish - start:.3f} segundos")  # Exibe o tempo total de execução
print(f"Memória atual: {memoria_atual / 1024:.3f} KB")  # Exibe a memória atual em KB
print(f"Pico de memória: {memoria_pico / 1024:.3f} KB")  # Exibe o pico de memória em KB