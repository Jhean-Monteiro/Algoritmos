# 8. Distribuição de Cadeiras
# Contexto: Uma sala de cinema tem 5 filas com 6 cadeiras cada.
# Tarefa: Crie uma matriz 5x6 e marque quais cadeiras estão ocupadas com “X” e quais estão
# livres com “O”.

filas = 5
cadeiras = 6
matriz = []

for i in range(filas):
    print(f"fila {i+1}")
    linha = []
    for j in range(cadeiras):
        while True:
            status = input(f"insira o status da cadeira {j+1} na fila {i+1} (O para livre ou X para ocupada)").upper()
            if status in ['O', 'X']:
                linha.append(status)
                break
            print("Status inválido. use O ou X'")
    matriz.append(linha)

print("Distribuição das cadeiras na sala de cinema:")
for i in range(filas):
    print(f"Fila {i+1}: {matriz[i]}")