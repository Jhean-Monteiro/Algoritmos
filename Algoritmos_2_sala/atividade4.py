'''
Estudo de Caso 4 - Controle de Vendas em uma Loja de Eletrônicos
Contexto do Problema
Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro
diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu
para criar um programa simples em Python para armazenar, analisar e gerar pequenos
relatórios sobre as vendas do dia.
O sistema precisa:
1. Guardar os produtos vendidos (nome e preço).
2. Mostrar o valor total arrecadado.
3. Identificar o produto mais caro e o mais barato do dia.
4. Permitir consultar se um produto específico foi vendido
'''

vendas = [] # cria uma lista vazia para armazenar os produtos vendidos
i = 0 # inicializa o contador para controlar a quantidade de vendas

while i < 5: # loop para registrar até 5 vendas (pode ajustar o limite)
    nome = input(f'digite o nome do produto {i+1} ')
    preço = float(input(f'digite o preço do {nome} R$')) # solicita o preço do produto e o converte para float
    vendas.append({'nome': nome, 'preço': preço}) # adiciona um dicionário com o nome e preço na lista
    i = i + 1

total = sum(item["preço"] for item in vendas) # calcula o total somando os preços de todos os itens
mais_caro = max(vendas, key=lambda x: x["preço"]) # identifica o produto mais caro usando uma função lambda para comparar os preços
mais_barato = min(vendas, key=lambda x: x["preço"]) # identifica o produto mais barato usando uma função lambda para comparar os preços

print(f"valor total arrecadado: R$ {total:.2f}") # exibe o total com duas casas decimais
print(f"produto mais caro: {mais_caro['nome']} (R$ {mais_caro['preço']:.2f})") # exibe o produto mais caro
print(f"produto mais barato: {mais_barato['nome']} (R$ {mais_barato['preço']:.2f})") # exibe o produto mais barato

consulta = input('digite o nome de um produto para consultar se foi vendido: ')
encontrado = any(item['nome'].lower() == consulta.lower() for item in vendas) # veridica se o produto está na lista (ignorando maiusculas e minusculas) '.lower()' converte ambos (nome e consulta) para minúsculas para ignorar diferenças de maiusculas/minusculas

print(f"o produto '{consulta}' {'foi' if encontrado else 'não foi'} vendido hoje.") # resultado da consulta