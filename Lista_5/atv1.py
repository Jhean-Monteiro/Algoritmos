'''
Lista de Exercícios com Matrizes – 
Aplicações Reais 
1. Controle de Temperatura de Salas 
Contexto: Uma empresa monitora a temperatura de 5 salas, 3 vezes ao dia. 
Tarefa: Armazene as temperaturas em uma matriz 5x3. Calcule a temperatura média de cada 
sala. 
'''

sala = 5
vezes = 3
matriz = []
dia = 0
for i in range(sala):
    dia += 1
    vez = 0
    linha = []
    for j in range(vezes):
        vez += 1
        linha.append(int(input(f"Dia: {dia}: insira a temperatura {vez}: ")))
    matriz.append(linha)

print(matriz)

lista = []
for item in matriz:
    for j in item:
        lista.append(j)
        
media = sum(lista) / len(lista)
print(f"a media é: {media}")