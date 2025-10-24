# 7. Vendas Semanais
# Contexto: Uma cafeteria registra vendas de 5 produtos durante 7 dias.
# Tarefa: Armazene os valores em uma matriz 5x7 e calcule a receita total semanal de cada
# produto.

produtos = 5
dias = 7

# produtos = 3
# dias = 3
matriz = []

for i in range(produtos):
    print(f"Produto {i+1}")
    linha = []
    
    for j in range(dias):
        while True:
            try:
                vendas = int(input(f"Insira a quantidade vendida do produto {i+1} no dia {j+1}: "))
                if vendas >= 0: # verifica se quantidade vendida não é negativa
                    break
                print(f"Quantidade não pode ser negativa. Tente novamente.")

            except ValueError:
                print("Por favor, insira um número inteiro válido.")
        linha.append(vendas)
    matriz.append(linha)


# coletando os preços dos produtos e calculando a receita total semanal
print("Coletando preços dos produtos:")
preço_produtos = []
for i in range(produtos):
    while True:
        try:
            preço = float(input(f"Insira o preço unitário do produto {i+1} (ex: 5.50): "))
            if preço >= 0:
                break
            print("preço não pode ser negativo. tente novamente.")

        except ValueError:
            print("por favor, insira um número válido")
    preço_produtos.append(preço)


# fazendo o calculo da receita total semanal de cada produto
print("Receita total semanal de cada produto:")
for i in range(produtos):
    total_vendido = sum(matriz[i])
    receita = total_vendido * preço_produtos[i]
    print(f"Receita do produto {i+1}: R${receita:.2f}")


# exibindo a matriz para vizualização
print(f"\nMatriz de vendas (produto x dia): ")
for i in range(produtos):
    print(f"Produto {i+1}: {matriz[i]}")