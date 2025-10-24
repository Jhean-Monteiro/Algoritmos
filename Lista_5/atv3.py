# 3. Agenda Semanal
# Contexto: Um consultório possui 5 dias de atendimento e 3 horários por dia.
# Tarefa: Armazene os nomes dos pacientes em uma matriz 5x3 e exiba a agenda completa

dias = 5
horarios = 3
agenda = []

for i in range(dias):
    print(f"Dia {i+1}:") # exibe o numero do dia (1 a 5)
    linha = [] # cria uma lista vazia para armazenar os horários de um dia
    for j in range(horarios): # loop interno para iterar sobre os 3 horários
        nome = input(f"Insira o nome do paciente para o horário {j+1} do dia {i+1}: ")
        linha.append(nome)
    agenda.append(linha)

print("Agenda Semanal:")
for i in range(dias): # loop para iterar sobre os dias (linhas da matriz)
    print(f"Dia {i+1}: {agenda[i]}") # exibe o número do dia e a lista de pacientes daquele dia
