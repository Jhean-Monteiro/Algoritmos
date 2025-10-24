# 5. Registro de Pontos em Jogos
# Contexto: Uma liga de esportes registra pontos de 3 times em 4 jogos.
# Tarefa: Crie uma matriz 3x4 com os pontos e determine qual time teve maior pontuação total.

times = 3
jogos = 4
matriz = []

for i in range(times):
    print(f"Time {i+1}:")
    linha = []
    for j in range(jogos):
        pontos = int(input(f"Insira os pontos do time {i+1} no jogo {j+1}: "))
        linha.append(pontos)
    matriz.append(linha)

maior_pontuacao = 0
time_maior_pontuacao = 0

for i in range(times):
    total_time = sum(matriz[i])
    print(f"Total de pontos do time {i+1}: {total_time}")
    if total_time > maior_pontuacao:
        maior_pontuacao = total_time
        time_maior_pontuacao = i + 1

print(f"O time com maior pontuação é o time {time_maior_pontuacao} com {maior_pontuacao} pontos.")



print(f"Matriz de pontos (Time x Jogo): ")
for i in range(times):
    print(f"Time {i+1}: {matriz[i]}")