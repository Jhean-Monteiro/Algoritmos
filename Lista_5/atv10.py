# 10. Registro de Chuva
# Contexto: Uma estação meteorológica registra chuva em 7 dias, para 3 cidades.
# Tarefa: Crie uma matriz 3x7 com os valores de chuva (mm) e determine qual cidade teve mais
# chuva na semana.

cidades = 3
dias = 7
matriz = []

for i in range(cidades):
    print(f"Cidade {i+1}:")
    linha = []
    for j in range(dias):
        while True:
            try:
                chuva = float(input(f"Insira a quantidade de chuva (mm) no dia {j+1} para a cidade {i+1}: "))
                if chuva >= 0:
                    break
                print("A quantidade de chuva não pode ser negativa. Tente novamente.")

            except ValueError:
                print("Por favor, insira um número válido.")
        linha.append(chuva)
    matriz.append(linha)


maior_chuva = 0
cidade_maior_chuva = 0

for i in range(cidades):
    total_chuva = sum(matriz[i])
    print(f"total de chuva na cidade {i+1}: {total_chuva:.2f} mm")
    if total_chuva > maior_chuva:
        maior_chuva = total_chuva
        cidade_maior_chuva = i+1

print(f"A cidade com maior quantidade de chuva na semana é a cidade {cidade_maior_chuva} com {maior_chuva:.2f} mm.")

print("Matriz de chuva (cidade x dia0):")
for i in range(cidades):
    print(f"Cidade {i+1}: {[round(x, 2) for x in matriz[i]]}")