# 1.Tratamento de exceções básicas: Escreva um programa que peça ao usuário dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir um valor inválido ou tentar dividir por zero, o programa deve exibir uma mensagem de erro apropriada.

try:
    numero = int(input("Digite um Número (inteiro): "))
    numero2 = int(input("Digite mais um Número (inteiro): "))

    divisão = numero/numero2

except ValueError:
    print("Digite apenas números inteiros!")

except ZeroDivisionError:
    print("Não é possível realizar divisões por Zero!")

else:
    print(f"o resultado é {divisão}")

finally:
    print("programa encerrado!")
