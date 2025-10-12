import random
import time
import tracemalloc

tracemalloc.start()
start = time.time()

# 11. Busca em Lista de Dicionários 
# • Dada uma lista de dicionários representando pessoas ({"nome": "Ana", "idade": 
# 25}), implemente uma busca linear para encontrar a pessoa com nome "João". 

def buscaPessoaPorNome(lista, nome_procurado):
    for indice, pessoa in enumerate(lista):
        if pessoa["nome"] == nome_procurado:
            return indice, pessoa
    return -1, None


lista_pessoas = [
    {"nome": "Gioliano", "idade": 30},
    {"nome": "João", "idade": 31},
    {"nome": "Sergio", "idade": 39},
    {"nome": "Jhean", "idade": 20},
    {"nome": "Diego", "idade": 30},
]

nome = "Gioliano"
indice, pessoa = buscaPessoaPorNome(lista_pessoas, nome)

if indice != -1:
    print(f"Pessoa encontrada no ínice {indice}: {pessoa}")
else:
    print(f"Pessoa com nome '{nome}' não foi encontrada na lista")


time.sleep(2)
#-------------------------------------------------------------------------------------------------------




# 12. Jogo: Adivinhe o Número (Busca Binária) 
# • O computador escolhe um número entre 1 e 100. O jogador tenta adivinhar, e o 
# computador responde se é maior ou menor. Use lógica de busca binária para resolver 
# com o menor número de tentativas. 

# Função principal do jogo
def adivinhe_o_numero():
    # Computador escolhe um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    pos_ini = 1
    pos_fim = 100

    print("\n\nBem-vindo ao jogo Adivinhe o Número!")
    print("Pensei em um número entre 1 e 100. Tente adivinhá-lo!")
    print("Dica: Use a estratégia de busca binária, escolhendo o meio do intervalo a cada tentativa.")

    while True:
        time.sleep(1)
        # # Sugere o palpite ideal (meio do intervalo) para ajudar o jogador
        # palpite_sugerido = (pos_ini + pos_fim) // 2
        # print(f"Intervalo atual: [{pos_ini}, {pos_fim}]")
        # print(f"Sugestão de palpite (meio do intervalo): {palpite_sugerido}")

        # Solicita o palpite do jogador
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        # Verifica se o palpite está dentro do intervalo
        if palpite < pos_ini or palpite > pos_fim:
            print(f"Seu palpite deve estar entre {pos_ini} e {pos_fim}. Tente novamente.")
            continue

        # Fornece feedback com base no palpite
        if palpite == numero_secreto:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("O número é MAIOR que seu palpite.")
            pos_ini = palpite + 1  # Ajusta o intervalo (descarta números menores)
        else:
            print("O número é MENOR que seu palpite.")
            pos_fim = palpite - 1  # Ajusta o intervalo (descarta números maiores)

        # Verifica se o intervalo colapsou
        if pos_ini > pos_fim:
            print(f"O número era {numero_secreto}. O intervalo colapsou, jogo encerrado em {tentativas} tentativas!")
            break

# Executa o jogo
adivinhe_o_numero()


'''
def adivinhe_o_numero():
    lista = []
    numero_secreto = random.randint(1, 1000000) # computador escolhe um numero aleatorio
    tentativas = 0
    pos_ini = 1
    pos_fim = 1000000

    print("bem-vindo ao jogo Advinhe o Número!")
    print("Pensei em um número entre 1 a 1000000. tente adivinhar!")
    time.sleep(0.5)

    while pos_ini <= pos_fim:
        palpite = (pos_ini  + pos_fim) // 2
        print(f"Minha sugestão: {palpite}")
        time.sleep(0.5)

        resposta = input("seu palpite está correto, maior ou menor? (digite 'correto', 'maior' ou 'menor'): ").lower()
        tentativas += 1

        if resposta == "correto":
            print(f"Parabens! você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
            return
        elif resposta == "maior":
            pos_ini = palpite +1
        elif resposta == "menor":
            pos_fim = palpite -1
        else:
            print("Por favor, digite 'correto', 'maior' ou 'menor'.")
            tentativas -= 1
    print(f"O número era {pos_ini}! Adivinhado em {tentativas} tentativas!")

adivinhe_o_numero()
'''


#-----------------------------------------------------------------------------------------------------------------------



# 13. Buscar Produtos por Preço 
# • Dada uma lista de produtos com preços, implemente uma busca para encontrar todos os 
# produtos com um determinado preço. 

def buscarProdutosPorPreco(lista_produtos, preco_procurado):
    produtos_encontrados = []
    for produto in lista_produtos:
        if produto["preço"] == preco_procurado:
            produtos_encontrados.append(produto)
    return produtos_encontrados

lista_produtos = [
    {"nome": "camiseta", "preço": 29.99},
    {"nome": "calça", "preço": 59.99},
    {"nome": "tênis", "preço": 99.99},
    {"nome": "boné", "preço": 29.99},
    {"nome": "jaqueta", "preço": 79.99},
    {"nome": "meia", "preço": 9.99},
    {"nome": "camisa estampada", "preço": 29.99},
]


preco_procurado = float(input("Digite o preço a ser procurado: "))
produtos_encontrados = buscarProdutosPorPreco(lista_produtos, preco_procurado)

if produtos_encontrados:
    print(f"Produtos encontrados com preço {preco_procurado}:")
    for produto in produtos_encontrados:
        print(f"- {produto['nome']} (Preço: {produto['preço']})")
else:
    print(f"Nenhum produto encontrado com preço {preco_procurado}.")



#------------------------------------------------------------------------------------------------------------------



# 14. Implementar sua própria função index() 
# • Crie uma função meu_index(lista, valor) que funcione como o método 
# list.index(), usando busca sequencial.

def meu_index(lista, valor):
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    return -1

valor = int(input("digite um valor: "))
lista = (random.randint(1,10000) for i in range(100000))
resultado = meu_index(lista, valor)
if resultado != -1:
    print(f"o valor {valor} foi encontrado no indice {resultado}")
else: 
    print(f"o valor {valor} não foi encontrado na lista")

    


finish = time.time()  # Registra o tempo final
memoria_atual, memoria_pico = tracemalloc.get_traced_memory()  # Obtém memória atual e pico
tracemalloc.stop()  # Para a medição de memória

print(f"\nTempo de execução: {finish - start:.3f} segundos")  # Exibe o tempo total de execução
print(f"Memória atual: {memoria_atual / 1024:.3f} KB")  # Exibe a memória atual em KB
print(f"Pico de memória: {memoria_pico / 1024:.3f} KB")  # Exibe o pico de memória em KB



