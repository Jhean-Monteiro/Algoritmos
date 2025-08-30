# 1. Cálculo de Complexidade Simples 
# Escreva um algoritmo que conte quantas operações básicas (somas) são executadas para 
# calcular a soma dos números de 1 até n. Exiba o resultado e compare com a fórmula matemática 
# bn*(n+1)/2.

numero = int(input("digite um numero: "))

soma_loop = 0
contador = 0
for i in range (1, numero+1):
    soma_loop += i
    contador += 1

formula = numero * (numero+1) // 2

print(f'soma feita com loop: {soma_loop}')

print(f'numero de operacoes (somas) feitas: {contador}')

print(f'soma calculada pela formula {formula}')