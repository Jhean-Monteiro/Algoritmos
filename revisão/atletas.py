atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["natação", "corrida"],
        "treinos": {"natação": 12, "corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["musculação", "yoga", "pilates"],
        "treinos": {"musculação": 15, "yoga": 10, "pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["corrida", "ciclismo"],
        "treinos": {"corrida": 20, "ciclismo": 10}
    }
]

# 1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte
# específico.

def media(esporte):
    idades = []
    for atleta in atletas:
        if esporte in atleta["modalidades"]:
            idades.append(atleta["idade"])
    if idades: # verifica se a alista de idades não está vazia
        media = sum(idades) / len(idades)
    print(media)

media("musculação")


# 2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou.

def esporte_mais_treinado(nome_atleta):
    for atleta in atletas:
        if atleta["nome"] == nome_atleta:
            if atleta["treinos"]: # verifica se o dicionário 'treinos' não está vazio
                esporte_max = max(atleta["treinos"].items(), key=lambda x: x[1])[0] # encontra o esporte com maior numero de treinos usando max(), com key=lambda x: x[1] para comparar os valores e [0] para pegar a chave (esporte)
                print(esporte_max)
                # return esporte_max
    # return "atleta não encontrado"

esporte_mais_treinado("Mariana")
# print(esporte_mais_treinado("Mariana"))


# 3. Monte uma lista com os atletas que praticam mais de 2 modalidades e exiba seus
# nomes.

def atletas_mais_duas_modalidades():
    atletas_selecionados = []
    for atleta in atletas:
        if len(atleta["modalidades"]) > 2:
            atletas_selecionados.append(atleta["nome"])

    print(atletas_selecionados)

atletas_mais_duas_modalidades()