# 1. Faça um programa que leia dois números e mostre qual é o maior. 


numero = int(input("insira um número: "))

numero2 = int(input("insira um número: "))

if numero > numero2:
    print(f'o numero {numero} é meior que o numero {numero2}')

elif numero2 > numero:
    print(f'o numero {numero2} é meior que o numero {numero}')

else:
    print('os números são iguais')