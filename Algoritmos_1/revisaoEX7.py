# 3. Estatísticas de Notas 
# Leia as notas de uma turma e: 
# • Calcule a média; 
# • Mostre a maior e a menor nota; 
# • Exiba o percentual de alunos acima da média.

notas = []
quantidade = int(input('quantos alunos há na turma? '))
for i in range(quantidade):
    nota = float(input(f'digite a nota do aluno {i+1}: '))
    notas.append(nota)

media = sum(notas) / quantidade
maior = max(notas)
menor = min(notas)

acima_media = [n for n in notas if n > media]
percentual = (len(acima_media) / quantidade) * 100

print(f'media da turma: {media:.2f}')
print(f'maior nota {maior}')
print(f'menor nota {menor}')
print(f'percentual de alunos acima da media: {percentual:.2f}')