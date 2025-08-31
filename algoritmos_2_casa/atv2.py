# Caso2: Distâncias em Km
# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

import math # importa o modulo math para usar a função ceil

viagens = [] # cria uma lista vazia para armazenar as distancias das viagens
i = 0 # inicializa o contador para controlar o numero de viagens

while i < 6: # loop até registrar 6 viagens
    distancia = float(input(f'digite a distancia da viagem {i + 1} em KM ')) # solicita a distancia e converte para float
    viagens.append(distancia) # adiciona a distancia a lista
    i += 1

total = sum(viagens) # calcula a distancia total somando todas as distancias
maior_distancia = max(viagens) # usa max para encontrar a maior distancia na lista
menor_distancia = min(viagens) # usa min para encontrar a menor distancia na lista
media = math.ceil(sum(viagens) / len(viagens)) # calcula a media e arredonda para cima usando math.ceil

print(f"distancia total percorrida: {total} km")
print(f"maior distancia: {maior_distancia} KM")
print(f"menor distancia: {menor_distancia} KM")
print(f"media das distancias (arredondada pra cima): {media} KM")