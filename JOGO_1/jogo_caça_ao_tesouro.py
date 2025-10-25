import random

# PS: isso aqui foi só pra fazer um teste
def exibir(parametrokkkkk):
    print(parametrokkkkk)

alcance = range
inteiro = int
entrada = input
aleatorio = random
DeuErrado = ValueError



''' INICIO: '''

tabuleiro = [["~" for i in alcance(5)] for i in alcance(5)] # cria a matriz 5x5

# escolhe uma linha e coluna aleatoria
tesouro_linha = aleatorio.randint(0, 4)
tesouro_coluna = aleatorio.randint(0, 4)
exibir(tesouro_linha)
exibir(tesouro_coluna)

tentativas = 7
for tentativa in alcance(tentativas):
    exibir("=== Tabuleiro === ")
    for linha in tabuleiro:
        exibir(" ".join(linha)) # .join() deixa a matriz mais bonitinha no console

    exibir(f"\n tentativa {tentativa + 1} de {tentativas}") # exibe a tentativa atual

    while True:  # inicia o loop de entrada da linha
        try:
            linha = inteiro(entrada("Escolha a linha (0-4): "))  # entrada de dados para inserir a linha
            if 0 <= linha <= 4:  # verifica se a linha digitada pelo usuário está presente na matriz (no tauleiro)
                break
            exibir("o numero deve ser entre 0 e 4.")  # mensagem de erro
        except DeuErrado:
            exibir("por favor, insira um número válido.")  # se digitar algo diferente de um numero, vai exibir isso aqui

    while True:  # inicia o loop para entrada da coluna
        try:
            coluna = inteiro(entrada("Escolha a coluna (0-4): "))  # pede a coluna pro usuário
            if 0 <= coluna <= 4:  # verifica se a coluna está presente na matriz
                break
            exibir("o numero deve ser entre 0 e 4.")  # mensagem de erro 
        except DeuErrado:
            exibir("por favor, insira um número válido.")  # se digitar algo diferente de um numero, vai exibir isso aqui

    if linha == tesouro_linha and coluna == tesouro_coluna:  # se o usuario acertou a localização do tesouro
        tabuleiro[linha][coluna] = "T"  #  marca a localização do tesouro com "T"
        exibir("\n=== Tabuleiro ===")  # exibe o tabuleiro atualizado
        for linha in tabuleiro:
            exibir(" ".join(linha))
        exibir("Parabéns! Você encontrou o tesouro!")  # Mensagem de vitória
        break

    else:  # se errar o tesouro
        tabuleiro[linha][coluna] = "X"  # marca a tentativa com "X"
        dica = ""  # inicializa a string de dica
        if linha < tesouro_linha:  # se o tesouro estiver mais abaixo...
            dica += "mais para baixo"
        elif linha > tesouro_linha:  # se o tesouro estiver mais acima...
            dica += "mais para cima"
        if coluna < tesouro_coluna:  # se o tesouro estiver a direita...
            dica += " e mais para a direita"
        elif coluna > tesouro_coluna:  # se o tesouro estiver na esquerda...
            dica += " e mais para a esquerda"
        exibir(f"O tesouro está {dica}.")  # mostra a dica


if tentativa == tentativas - 1:
    exibir("\n=== Resultado Final ===")  # mostra o tabuleiro final
    for linha in tabuleiro:
        exibir(" ".join(linha))
    exibir(f"Game Over! O tesouro estava em ({tesouro_linha}, {tesouro_coluna})")