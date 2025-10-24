# 4. Controle de Estoque
# Contexto: Uma loja possui 4 produtos e verifica o estoque em 3 lojas diferentes.
# Tarefa: Crie uma matriz 4x3 com as quantidades de cada produto em cada loja e calcule o total
# de cada produto.

produtos = 4
lojas = 3
matriz = []

for i in range(produtos):
    print(f"Produto {i+1}: ")
    linha = [] # cria uma lista vazia para armazenar as quantidades do produto nas lojas
    for j in range(lojas):
        quantidade = int(input(f"Insira a quantidade do produto {i+1} na loja {j+1}: "))
        linha.append(quantidade)
    matriz.append(linha)

print("Total de cada produto: ")
for i in range(produtos):
    total_produto = sum(matriz[i])
    print(f"Total do produto {i+1}: {total_produto}")

print("Matriz de estoque (Produto x Loja):")
for i in range(produtos):
    print(f"Produto {i+1}: {matriz[i]}")

# print(matriz)