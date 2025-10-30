import random

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = [[0 for i in range(colunas)] for i in range(linhas)] # matriz com zeros
    minas = 0 # contador de minas

    while minas < qtd_minas:
        linha = random.randint(0, linhas - 1) # coloca linha aleatoria
        coluna = random.randint(0, colunas - 1) # coloca coluna aleatoria
        if tabuleiro[linha][coluna] != "*": # verifica se a posição não tem mina
            tabuleiro[linha][coluna] = "*" # coloca a mina
            minas = minas + 1
    return tabuleiro


def mostrar_tabuleiro(tabuleiro, revelado): # def pra exibir tabuleiro
    print("=== Tabuleiro ===") # cabeçalho
    for i in range(len(tabuleiro)): # percorre as linhas
        for j in range(len(tabuleiro[0])): # percorre as colunas
            if not revelado[i][j]:
                print(".", end=" ") # mostra um ponto para posições ocultas
            else:
                print(tabuleiro[i][j], end=" ") # exibe o valor da posição
        print() # nova linha após cada linha do tabuleiro

def contar_minas_vizinhas(tabuleiro, linha, coluna): # conta minas nas posições vizinhas
    conta = 0
    for i in range(max(0, linha - 1), min(len(tabuleiro[0]), linha + 2)): # iteras linhas vizinhas
        for j in range(max(0, coluna - 1), min(len(tabuleiro), coluna + 2)): # iteras colunas vizinhas 
            if tabuleiro[i][j] == "*": # verifica se há mina
                conta = conta + 1
    return conta

def jogar(tabuleiro): 
    linhas = len(tabuleiro) # obtem qtd de linhas
    colunas = len(tabuleiro[0]) # obtem qtd de colunas
    revelado = [[False for i in range(colunas)] for i in range(linhas)]
    celulas_seguras = linhas * colunas - tabuleiro.count("*")

    while True: # principal loop do jogo
        mostrar_tabuleiro(tabuleiro, revelado) # exibe tabuleiro atual
        try:
            linha = int(input("Escolha a linha (0-4): "))  # Pede linha
            coluna = int(input("Escolha a coluna (0-4): "))  # Pede coluna
            if 0 <= linha < linhas and 0 <= coluna < colunas and not revelado[linha][coluna]:  # Valida entrada
                revelado[linha][coluna] = True  # Marca como revelada
                if tabuleiro[linha][coluna] == "*":  # Verifica se há mina
                    mostrar_tabuleiro(tabuleiro, revelado)  # Exibe tabuleiro final
                    print("Game Over! Você explodiu uma mina.")  # Mensagem de derrota
                    break
                else:
                    minas_vizinhas = contar_minas_vizinhas(tabuleiro, linha, coluna)  # Conta minas vizinhas
                    if minas_vizinhas > 0:  # Se houver minas vizinhas
                        tabuleiro[linha][coluna] = minas_vizinhas  # Atualiza com número de minas
                    celulas_seguras -= 1  # Decrementa células seguras restantes
                    if celulas_seguras == 0:  # Verifica vitória
                        mostrar_tabuleiro(tabuleiro, revelado)  # Exibe tabuleiro final
                        print("Vitória! Você abriu todas as células seguras.")  # Mensagem de vitória
                        break
            else:
                print("Coordenada inválida ou já revelada. Tente novamente.")  # Mensagem de erro
        except ValueError:
            print("Entrada inválida. Use números entre 0 e 4.")  # Trata erro de entrada

# Configurações do jogo
tabuleiro = criar_tabuleiro(5, 5, 5)  # Cria tabuleiro 5x5 com 5 minas
jogar(tabuleiro)  # Inicia o jogo