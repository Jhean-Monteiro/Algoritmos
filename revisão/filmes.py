filmes = [

    {

        "titulo": "Inception",

        "diretor": "Christopher Nolan",

        "bilheteria": 830,

        "avaliações": [9, 10, 8, 9, 10]

    },

    {

        "titulo": "Avengers: Endgame",

        "diretor": "Anthony Russo",

        "bilheteria": 2797,

        "avaliações": [9, 9, 10, 10, 9]

    },

    {

        "titulo": "The Dark Knight",

        "diretor": "Christopher Nolan",

        "bilheteria": 1005,

        "avaliações": [10, 10, 9, 10, 10]

    },

    {

        "titulo": "Jurassic Park",

        "diretor": "Steven Spielberg",

        "bilheteria": 1029,

        "avaliações": [8, 9, 9, 8, 9]

    }

]

# 1. Top 3 maiores bilheterias
# o Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior
# bilheteria.

def top_bilheteria_filmes(filmes):
    bilheterias = [(filme["titulo"], filme["bilheteria"]) for filme in filmes]
    bilheterias_ordenadas = sorted(bilheterias, key=lambda x: x[1], reverse=True)
    print(bilheterias_ordenadas[:3])

top_bilheteria_filmes(filmes)



# 2. Top 3 melhores avaliados
# o Crie uma função top_avaliacao(filmes) que calcule a média das avaliações de
# cada filme e retorne os 3 melhores.

def top_avaliações(filmes):

    medias = {}
    for filme in filmes:
        titulo = filme["titulo"]
        avaliações = filme["avaliações"]
        media = sum(avaliações) / len(avaliações) if avaliações else 0
        medias[titulo] = media
    ranking = sorted(medias.items(), key=lambda x: x[1], reverse=True)
    print(ranking[:3])

top_avaliações(filmes)



# 3. Bilheteria por diretor
# o Crie uma função bilheteria_por_diretor(filmes) que retorne um dicionário onde a
# chave é o diretor e o valor é o total de bilheteria de todos os seus filmes.

def bilheteria_por_diretor(filmes):
    bilheteria_diretores = {}
    for filme in filmes:
        diretor = filme["diretor"]
        bilheteria = filme["bilheteria"]
        bilheteria_diretores[diretor] = bilheteria_diretores.get(diretor, 0) + bilheteria
    print(bilheteria_diretores)

bilheteria_por_diretor(filmes)



# 4. Campeão absoluto
# o Crie uma função campeao(filmes) que mostre qual filme é a melhor combinação
# de bilheteria alta e avaliação média alta.

def campeão(filmes):
    pontuações = []
    for filme in filmes:
        titulo = filme["titulo"]
        bilheteria = filme["bilheteria"]
        avaliações = filme["avaliações"]
        media = sum(avaliações) / len(avaliações) if avaliações else 0
        pontuação = (bilheteria / 3000) * 0.5 + (media / 10) * 0.5
        pontuações.append((titulo, pontuação))
    campeão = max(pontuações, key=lambda x: x[1])[0]
    print(campeão)

campeão(filmes)