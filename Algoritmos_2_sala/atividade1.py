'''
Estudo de Caso 1 – Temperaturas da Semana
Enunciado:
Crie um programa que:
1. Receba as temperaturas de 7 dias e armazene em uma lista.
2. Mostre a média das temperaturas da semana.
3. Informe o dia mais quente e o dia mais frio.
4. Mostre quantos dias ficaram acima da média.Estudo de Caso 1 – Temperaturas da Semana
Enunciado:
Crie um programa que:
1. Receba as temperaturas de 7 dias e armazene em uma lista.
2. Mostre a média das temperaturas da semana.
3. Informe o dia mais quente e o dia mais frio.
4. Mostre quantos dias ficaram acima da média.
'''


dias = [1,2,3,4,5,6,7] # define a lista de dias da semana
temps = [] # cria uma lista vazia para armazenar as temperaturas
i = 0 # inicializa o contador para o loop

for dia in dias: # para cada dia na lista de dias
    temp = float(input(f'Insira aqui a temperatura do dia {dia}: ')) # entrada para colocar a temperatura e converter para float
    temps.append(temp) # adiciona a temperatura (temp) na lista de temperaturas (temps)
    i = i + 1 # contador de itens para a lista temps
    if i >= 7: # o loop vai repetir até esse valor atingir 7
        break # o loop para quando i chega a 7

media = sum(temps) / len(temps) # sum: soma os valores da lista e então divide po "len": o total de itens na lista (7)
maior = max(temps) # max: encontra o maior valor na lista
menor = min(temps) # min: encontra o menor valor na lista

acima_media = sum(1 for temp in temps if temp > media) # adiciona 1 para cada temperatura acima da média, e "sum" somas esses 1s para dar o total

print(f'a media das temperaturas da semana foi {media:}.2f') # 2f. = limita a dois digitos após a vírgula
print(f'maior temperatura: {maior}')
print(f'menor temperatura: {menor}')
print(f'quantidade de dias acima da média: {acima_media}')