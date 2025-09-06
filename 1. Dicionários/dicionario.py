lista = [10, 8]

dicionario = {
    "chave": 10,
    "key": 11,
}

print(dicionario["chave"])
print(dicionario["key"])

# aluno -> nome, curso, idade

aluno = {
    "nome": "fulano",
    "curso": "ESW",
    "idade": 26
}

print(aluno["curso"])

print(aluno.get("curso"))

personagem = {
    "personagens1" : { # chave
        "id":1,        
        "Nome": "Rick",
        "status": "alive",   # valor:
        "specie": "human",
},
    "personagens2" : {
        "id":2,
        "Nome": "Morty",
        "status": "alive",
        "specie": "human"
}

}


# print(personagens)

# personagens.pop("status") # retira status

# print(personagens)

# personagens["status"]="Dead" # adiciona dead no status


print(personagem)




produtos = {"arroz": "R$15", "feijão":"R$8","macarrão":"R$10"}

for chave,valor in produtos.items(): # produtos.items = função que pega chave e valor
    print(chave,valor) # imprime chave e valor