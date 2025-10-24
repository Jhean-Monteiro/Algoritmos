'''
2. Grade de Notas de Alunos 
Contexto: Uma turma de 4 alunos realizou 3 provas. 
Tarefa: Armazene as notas em uma matriz 4x3 e calcule a média de cada aluno e a média de 
cada prova. 
'''


alunos = 4
provas = 3
matriz = []

aluno = 0
for i in range(alunos):
    aluno += 1
    prova = 0
    linha = []
    for j in range(provas):
        prova += 1
        linha.append(int(input(f"insira a nota da prova {prova} do aluno {aluno}: ")))
    matriz.append(linha)

estudante = 0
notas = []
for aluno in matriz:
    estudante += 1
    for nota in aluno:
        notas.append(nota)
        media = sum(notas) / len(notas)
    print(f"a media do aluno {estudante} é: {media:.2f}")