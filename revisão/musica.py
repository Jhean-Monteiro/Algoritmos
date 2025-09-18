musicas = [
    {
        "titulo": "back in black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliações": [5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "stairway to heaven",
        "artista": "Led Zeppelin",
        "downloads": 8990,
        "avaliações": [5, 5, 4, 5, 5, 5]
    },
    {
        "titulo": "enter sandman",
        "artista": "Metallica",
        "downloads": 811,
        "avaliações": [5, 5, 5, 4, 4, 5, 5]
    }
]

# 1. Crie uma função que calcule a nota média de avaliação de cada música.

def media_avaliação_musica():
    medias = {} # cria um dicionario para armazenar o titulo da musica como chave e sua media como valor
    for musica in musicas: # para cada dicionario na lista de musicas
        titulo = musica["titulo"]
        avaliações = musica["avaliações"]
        media = sum(avaliações) / len(avaliações) if avaliações else 0 # calcula a media das avaliações (se a lista não estiver vazia)
        medias[titulo] = media
    print(medias)

media_avaliação_musica()


# 2. Crie uma função que mostre qual artista tem o maior número total de downloads
# somando todas as suas músicas.

def artista_mais_downloads():
    downloads_por_artista = {} # cria um dicionário para armazenar o nome de cada artista como chave e o total de downloads de suas musicas como valor
    for musica in musicas:
        artista = musica["artista"] # extrai o valor associado à chave "artista" de cada dicionário "musica", e armazena na variavel "artista" 
        downloads = musica["downloads"] # extrai o valor associado à chave "downloads" de cada dicionario "musica", que é o número de downloads dessa musica, e armazena na variavel (downloads)
        downloads_por_artista[artista] = downloads_por_artista.get(artista, 0) + downloads # atualiza o dicionario 'downloads_por_artista': usa get(artista, 0) para obter o valor atual do artista (ou 0 se o artista ainda não estiver no dicionario). soma o numero de "downloads" dessa musica, e atribui o novo total como valor para a chave "artista"
    if downloads_por_artista: # verifica se o dicionario "downloads_por_artista" contém pelo menos uma entrada (se há dados para processar)
        artista_max = max(downloads_por_artista.items(), key=lambda x: x[1])[0] # usa a função max() para encontrar a tupla (artista, total de downloads) com o maior valor; .items() converte o dicionário em uma lista de tuplas (ex: [("AC/DC", 6800), ("Led Zeppelin", 8990)]), key=lambda x: x[1] define que a comparação deve ser baseada no segundo elemento de cada tupla, (o total de downloads), e [0] extrai apenas o nome do artista da tupla vencedora
        print(artista_max)
    # print("nenhum artista encontrado")

artista_mais_downloads()




# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das
# notas).

def ranking_musicas():
    medias = {}
    for musica in musicas:
        titulo = musica["titulo"]
        avaliações = musica["avaliações"]
        media = sum(avaliações) / len(avaliações) if avaliações else 0
        medias[titulo] = media
    if not medias:
        return []
    ranking = sorted(medias.items(), key=lambda x: x[1], reverse=True)
    print(ranking)

ranking_musicas()