'''
Estudo de Caso 3 – Analisando números pares e ímpares
Enunciado:
Escreva um programa que:
1. Receba 10 números inteiros digitados pelo usuário.
2. Separe-os em duas listas: pares e ímpares.
3. Exiba quantos números pares e ímpares foram digitados.
'''

numeros = [] # cria uma lista vazia para armazenar os números digitados pelo usuário
pares = [] # cria uma lista vazia para armazenar os números pares 
impares = [] # cria uma lista vazia para armazenar numeros impares
i = 0 # contador

while i < 10: # enquanto o contador for menor que 10
    num = int(input(f"digite o {i+1}° numero: ")) # solicita um numero e converte para inteiro
    numeros.append(num) # adiciona um número a lista geral
    if num % 2 == 0: # verifica se o número é par (divisível por 2 sem resto)
        pares.append(num) # adiciona o num par na lista pares

    else: # se não for par, é ímpar
        impares.append(num) # adiciona o num impar na lista impares

    i += 1 # aumenta o contador

    # o loop acima vai repetir até o i chegar em 10

print(f'quantidade de numeros pares: {len(pares)}') # exibe a quantidade de numeros pares com o len
print(f'quantidade de numeros impares: {len(impares)}') # exibe a qtdd de impares com len


# um extra:
print('pares digitados: ', pares)
print('impares digitados: ',impares)