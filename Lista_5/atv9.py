# 9. Planejamento de Exercícios
# Contexto: Uma academia planeja 3 tipos de exercícios para 4 alunos diferentes.
# Tarefa: Crie uma matriz 4x3 que registre quantas repetições cada aluno deve fazer e calcule o
# total de repetições de cada exercício.

alunos = 4
exercicios = 3
matriz = []

for i in range(alunos):
    print(f"Aluno {i+1}:")
    linha = []
    for j in range(exercicios):
        while True:
            try:
                repeticoes = int(input(f"Insira o número de repetições do exercício {j+1} para o aluno {i+1}: "))
                if repeticoes >= 0:
                    break
                print("O número de repetições não pode ser negativo!")

            except ValueError:
                print("por favor, insira um número inteiro válido.")
        linha.append(repeticoes)
    matriz.append(linha)



print("Total de repetições de cada exercício:")
for j in range(exercicios):
    total_exercicio = 0
    for i in range(alunos):
        total_exercicio += matriz[i][j]
    print(f"Total de repetições do exercício {j+1}: {total_exercicio}")

print("Matriz de repetições (Alunos x Exercício):")
for i in range(alunos):
    print(f"Aluno {i+1}: {matriz[i]}")