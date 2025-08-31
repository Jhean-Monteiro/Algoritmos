# Caso3: Supermercado – Controle de Estoque
# Um supermercado mantém uma lista de produtos e seus preços.
# • Cada item será representado como [nome, quantidade, preco_unitario].
# • O sistema deve:
# 1. Calcular o valor total em estoque.
# 2. Encontrar o produto de maior valor total (quantidade × preço).
# 3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5
# unidades.
# 4. Permitir buscar um produto pelo nome e retornar seus dados.

estoque = []
i = 0
while i < 3:
    nome = input(f'digite o nome do produto {i+1} ')
    quantidade = int(input(f'digite a quantidade de {nome}: '))
    preço_unitario = float(input(f'digite o preço unitario de {nome}: '))
    estoque.append([nome, quantidade, preço_unitario])
    i +=1

valor_total = sum(item[1] * item[2] for item in estoque)

produto_mais_valioso = max(estoque, key=lambda x: x[1] * x[2]) # usa a função lambda para comparar o valor total (quantidade x preço)

estoque_baixo = [item[0] for item in estoque if item [1] < 5] # cria uma lista apenas com os nomes onde a quantidade é menor que 5

# busca pelo nome
busca = input('digite o nome de um produto para consultar: ')
produto_encontrado = next((item for item in estoque if item[0].lower() == busca.lower()), None) # procura o produto (ignorando maiusculas/minusculas)

print(f'valor total em estoque: {valor_total:.2f}')
print(f'produto de maior valor total: {produto_mais_valioso[0]} (quantidade: {produto_mais_valioso[1]}, valor: R${produto_mais_valioso[1] * produto_mais_valioso[2]:.2f})')
print(f'produtos com estoque abaixo de 5 unidades: {estoque_baixo}')
if produto_encontrado:
    print(f"dado do produto'{busca}': Nome: {produto_encontrado[0]}, quantidade: {produto_encontrado[1]}, Preço unitario: R${produto_encontrado[2]:.2f}")

else:
    print(f"Produto '{busca}' não encontrado no estoque.")