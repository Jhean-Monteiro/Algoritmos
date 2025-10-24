# 6. Horários de Transporte
# Contexto: Um ponto de ônibus tem 4 linhas, cada uma com 3 horários.
# Tarefa: Armazene os horários em uma matriz 4x3 e permita que o usuário consulte os horários
# de uma linha específica.

linhas = 4
horarios = 3
matriz = []

for i in range(linhas):
    print(f"Linha {i+1}::")
    linha = []

    for j in range(horarios):
        horario = input(f"Insira o horário {j+1} da linha {i+1} (ex: 00:00): ")
        linha.append(horario)
    matriz.append(linha)

# exibindo a matriz completa para vizualização
print(f"Matriz de horários (Linha x Horário):")
for i in range(linhas):
    print(f"Linha {i+1}: {matriz[i]}")

# consultando os horários de uma linha específica
while True:
    try:
        consulta = int(input("Digite o número da linha (1 a 4) para consultar os horários (ou 0 para sair): "))

        if consulta == 0:
            print("Consulta encerrada.")
            break

        if 1 <= consulta <= linhas:
            print(f"Horários da linha {consulta}: {matriz[consulta - 1]}")

        else:
            print("Linha inválida. Digite um número entre 1 e 4.")


    except ValueError:
        print("Por fvor, digite um número inteiro válido.")