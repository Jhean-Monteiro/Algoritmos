# 2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário. 


numero = int(input("Escreva um número para ver a sua tabuada: "))
print(f"Tabuada do Número {numero}")
for i in range(1,11):
    resultado = numero * i

    print(f"{numero} vezes {i} = {resultado}")