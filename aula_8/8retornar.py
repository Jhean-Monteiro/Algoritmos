# Ler um arquivo CSV e retornar os dados como lista de dicionários.

import csv
with open('data.csv', 'r', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    dados = list(leitor)
    for linha in dados:
        print(linha)