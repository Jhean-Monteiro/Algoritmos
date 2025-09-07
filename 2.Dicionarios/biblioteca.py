# Caso6: Sistema de Biblioteca
# Implemente os códigos usando Dicionários.



# abaixo um dicionario onde a chave é o título do livro e o valor é outro dicionario com informações do usuário e dias emprestado
biblioteca = {
    "Dom Casmurro": {
        "usuario": "ana", "dias": 12
    },
    "1984": {
        "usuario": "Manoel", "dias": 4
    },
    "Meditações": {
        "usuario": "jhean", "dias": 20
    },
    "harry potter": {
        "usuario": "gabrielle", "dias": 7
    }
}

# 1. listar apenas os livros emprestados há mais de 7 dias
livro_acima_7 = [livro for livro, dados in biblioteca.items() if dados["dias"] > 7] # percorre os itens e pega só os livros com mais de 7 dias
print("livros emprestados há mais de 7 dias", livro_acima_7)

# 2. encontrar o livro emprestado há mais tempo
livro_mais_tempo = max(biblioteca, key=lambda x: biblioteca[x]["dias"]) # encontra vo livro com maior valor no campo "dias"
print("livro emprestado há mais tempo:", livro_mais_tempo, "-->", biblioteca[livro_mais_tempo])

# 3. gerar uma lista apenas com os nomes dos usuarios que tem livros emprestados
usuarios = [dados["usuario"] for dados in biblioteca.values()] # percorre os valores do dicionario e extrai apenas o campo "usuario"
print("usuários com livros emprestados:", usuarios)

# 4. calcular a média de dias de empréstimo
total_dias = sum(dados["dias"] for dados in biblioteca.values()) # soma todos os vallores do campo "dias"
media_dias  = total_dias / len(biblioteca) # divide pelo número de livros no dicionario
print("media de dias de emprestimo:", media_dias)