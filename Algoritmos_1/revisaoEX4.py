# 4. Desenvolva um programa que leia uma lista de números e mostre a média deles. 

entrada = input("insira os números separados por espaço: ")

numeros = [int(x) for x in entrada.split()]

media = sum(numeros) / len(numeros)




print(media)