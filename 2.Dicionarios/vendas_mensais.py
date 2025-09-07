# Análise de Vendas Mensais


# abaixo um dicionario onde a chave é o dia do mês e o valor é a quantidade de vendas
vendas = {
    1: 10,
    2: 15,
    3: 20,
    4: 5,
    5: 0,
    6: 8,
    7: 12,
    8: 25,
    9: 7,
    10: 18,
    }

# 1. calcular o total de vendas no mês
total_vendas = sum(vendas.values()) # soma todos os valores do dicionario
print("total de vendas no mês:", total_vendas)

# 2. descobrir o dia com mais vendas e o dia com menos vendas
dia_max = max(vendas, key=vendas.get) # encontra a chave (dia) com maior valor
dia_min = min(vendas, key=vendas.get) # encontra a chave (dia) com menor valor
print(f'dia com mais vendas', dia_max, "-->", vendas[dia_max])
print(f'dia com menos vendas', dia_min, "-->", vendas[dia_min])

# 3. calcular a media de vendas por dia
media_vendas = total_vendas / len(vendas) # soma dividido pelo numero de dias
print("Media de vendas por dia:", media_vendas)

# 4. listar os dias que tiveram vendas acima da media
dias_up_media = [dia for dia, qtd in vendas.items() if qtd > media_vendas] # percorre todos os pares (dia, quantidade) e pega só os dias com vendas acima da media
print("dias acima da media: ", dias_up_media)