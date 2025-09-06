import time
# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno

aluno = {
    "nome": "Jhean",
    "idade": "20",
    "curso": "ESW"
}

print("nome do aluno:", aluno["nome"]) # exibindo apenas o nome do aluno
time.sleep(0.5)


# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".

aluno["nota"] = 9.5 # adicionando a chave "nota" e atribuindo o valor "9,5"
del aluno ["idade"] # removendo a chave "idade"
print(f"dicionário atualizado: {aluno}")
time.sleep(0.9)


# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produots = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

produots = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
for k,v in produots.items(): # loop + função para exibir chave e valor
    print(k,':',v)
time.sleep(0.5)


# 4. Dado o dicionário aluno, verifique se existe a chave "curso"
if "curso" in aluno:
    print(f"A chave 'curso' existe no dicionário aluno")
else:
    print('a chave "curso" não existe')


# 5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome
# e nota.
# Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.

turma = {
    "aluno1" : {
        "nome": "Rowan",
        "nota": 10,
    },

    "aluno2" : {
        "nome": "victor",
        "nota": 9
    }
    
}

print(turma["aluno1"].get("nome"))
print(turma["aluno2"].get("nota"))
time.sleep(0.5)


# 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
# a. Adicione ao dicionário do carro a chave 'cor'.

carro = {
    "marca": "Toyota",
    "modelo": "Corola",
    "ano": "2020"
}
carro["cor"]="verde"
print(f'dicionário com carro: {carro}')



# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
# valor).

notas = {
    "Carlos" : {
        "10"
    },
    "Jhean" : {
        "01"
    },
    "João" : {
        "9"
    },
}

# c. Acesse a nota de um dos alunos e exiba.
print(f"Nota do Jhean: {notas["Jhean"]}")





# d. Remova um aluno do dicionário de notas.
del notas["João"]
print(f'dicionario de notas atualizado: {notas}')