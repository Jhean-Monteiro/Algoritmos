# 5.Simulação de transações: Crie um programa que simule uma transferência bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o saldo seja insuficiente, levante uma exceção do tipo ValueError com a mensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o usuário.

try:
    saldo = int(input("Insira o saldo da conta: "))
    transferencia = int(input("insira o valor da transferencia: "))

    if saldo < transferencia:
        print("você nem tem dinheiro meo")
    else:
        print(f"você tem grana. toma: R${transferencia:.2f}")

except:
    print("você não tem dinheiro o suficiente...")

