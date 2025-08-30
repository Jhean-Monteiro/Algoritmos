# 3. Crie uma função que verifique se um número é primo. 


def primo(numero):
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
num = int(input("digite um numero: "))

if primo(num):
    print(f"o numero {num} é um numero primo.")
else:
    print(f"o numero {num} não é um numero primo.")
