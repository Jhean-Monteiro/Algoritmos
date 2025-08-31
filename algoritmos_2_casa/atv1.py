'''
Caso1: Controle de Presença em Sala de Aula
Uma professora precisa registrar a presença dos alunos durante a semana.
• Cada dia da semana terá uma lista com os nomes dos presentes.
• No final, ela precisa:
1. Saber quais alunos estiveram presentes todos os dias.
2. Saber quais alunos faltaram em pelo menos um dia.
3. Saber o número total de presenças por aluno.
'''

dias_semana = ['segunda','terça','quarta','quinta','sexta']
presenças = {dia: [] for dia in dias_semana} # cria um dicionario vazio para cada dia com listas de presenças
i = 0 # inicializa o contador para controlar os dias

for dia in dias_semana:
    print(f'registro de presença para {dia}: ') 
    while True: # loop para adicionar alunos até o usuario decidir parar
        aluno = input("digite o nome do aluno presente (ou 'fim' para encerrar): ")
        if aluno.lower() == "fim": #verifica se o usuário quer encerrar
            break # sai do loop interno

        presenças[dia].append(aluno) # adiciona o aluno a lista de presença do dia
    i = i + 1 # aumenta o contador

# encontra alunos presentes todos os dias
presentes_todos_dias = set(presenças['segunda']) # converte a lista de segunda em um 'set' (conjunto) que remove duplicatas e permite operações como interseção
for dia in dias_semana [1:]: # itera sobre os outros dias
    presentes_todos_dias &= set(presenças[dia]) # '&' serve para fazer interseção de conjuntos, mantendo apenas os alunos que aparecem em ambos os 'sets' (presentes em todos os dias)
presentes_todos_dias = list(presentes_todos_dias) # converte o 'set' de volta para lista para exibição, pois 'set' não mantem ordem

# encontra alunos que faltaram em pelo menos um dia
todos_alunos = set().union(*[set(presenças[dia]) for dia in dias_semana]) # une todos os alunos de todos os dias
faltaram_ao_menos_um_dia = list(todos_alunos - set(presentes_todos_dias)) # diferença para encontrar quem não esteve todos od dias

#calcula o numero total de presenças por aluno
presenças_por_aluno = {}
for aluno in todos_alunos: # itera sobre todos os alunos únicos
    contagem = sum(aluno in presenças[dia] for dia in dias_semana) # conta quantas vezes o aluno apareceu
    presenças_por_aluno[aluno] = contagem # armazena a contagem no dicionario

# exibe os resultados
print('alunos presentes todos os dias', presentes_todos_dias)
print('alunos que faltaram em pelo menos um dia', faltaram_ao_menos_um_dia)
print('numero total de presenças por aluno', presenças_por_aluno)
