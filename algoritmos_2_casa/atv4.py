# Caso4: Análise de Vendas Mensais
# Uma loja online registra o número de vendas de cada dia do mês em uma lista.
# • Exemplo: [10, 15, 20, 5, 0, 8, ...]
# O gerente precisa:
# 1. Calcular o total de vendas no mês.
# 2. Descobrir o dia com mais vendas e o dia com menos vendas.
# 3. Calcular a média de vendas por dia.
# 4. Listar os dias que tiveram vendas acima da média.

vendas = []
i = 0

while i < 10:
    venda = int(input(f"digite o numero de vendas {i+1}: "))
    vendas.append(venda)
    i+=1

total_vendas = sum(vendas)
dia_mais_vendas = vendas.index(max(vendas)) + 1
dia_menos_vendas = vendas.index(min(vendas)) + 1
media_vendas = sum(vendas) / len(vendas)
dias_acima_media = [i + 1 for i in range(len(vendas)) if vendas[i] > media_vendas]

print(f'total de vendas no mes: {total_vendas}')
print(f'dia com mais vendas: Dia {dia_mais_vendas} ({max(vendas)} vendas)')
print(f'dia com menos vendas: Dia {dia_menos_vendas} ({min(vendas)} vendas)')
print(f'media de vendas por dia: {media_vendas:.2}')
print(f'dias com vendas acima da media: {dias_acima_media}')