# Estudo de Caso : Cadastro de Produtos
# Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve
# conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e
# manipular essas informações.
# Exemplo:
# produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
# print(f"O produto {produto["nome"]} custa R${produto["preco"]}")


produtos = [] # cria uma lista vazia pra registrar multiplos produtos como dicionarios
i = 0 # Inicializa o contador para controlar o número de produtos
while i < 2: # para registrar dois produtos (pode ajustar o limite)
    produto = {
        "nome": input(f"Digite o nome do produto {i+1}: "), # solicita o nome do produto
        "preço": float(input(f"digite o preço do produto: R$ ")), # solicita e converte o preço para float
        "estoque": int(input(f"Digite a quantidade em estoque: ")) # solicita e converte a quantidade para inteiro
    }

    produtos.append(produto) #
    i = i+1 # atualiza o valor de i

# exibir as informações de cada produto:
for produto in produtos: # para cada dicionario "produto" dentro da lista "produtos:"
    print(f"o produto {produto["nome"]} custa R${produto["preço"]:.2f}") # exibe o nome e preço com duas casas decimais



# Estudo de Caso 2: Agenda Telefônica
# Uma agenda pode ser representada como um dicionário em que as chaves são os nomes
# das pessoas e os valores são os números de telefone.
# Exemplo:
# agenda = {"Maria": "99999-1234", "João": "98888-5678"}
# print("Telefone da Maria:", agenda["Maria"])

agenda = {} # cria um dicionario para a agenda telefonica
i = 0 # inicia contador para controlar o numero de contatos

while i < 2: # itera para registrar 2 contatos
    contato = input(f"digite o nome do contato {i+1} ")
    telefone = input(f"digite o telefone de {contato}: ")
    agenda[contato] = telefone # adiciona o par nome-telefone ao dicionário agenda
    i +=1 # aumenta o contador

# exibe o telefone de cada contato:
for nome, telefone in agenda.items(): # chama os pares chave e valor do dicionario agenda
    print(f"telefone de {nome}: {telefone}")