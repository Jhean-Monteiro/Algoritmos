pedidos = [
    {
        "cliente": "Gioliano",
        "itens": [
            {"prato": "Lasanha", "preço": 60},
            {"prato": "Suco de Laranja", "preço": 8},
            {"prato": "Pizza", "preço": 40},
        ]
    },
    {
        "cliente": "Jhean",
        "itens": [
            {"prato": "Pizza", "preço": 40},
            {"prato": "Refrigerante", "preço": 7},
            {"prato": "Sobremesa", "preço": 100},
           
        ]
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preço": 40},
            {"prato": "Suco de Laranja", "preço": 8}
        ]
    }
]

# 1. CRIE UMA FUNÇÃO QUE RECEBA O NOME DE UM CLIENTE E RETORNE O VALOR TOTAL GASTO
# (SOMANDO TODOS OS ITENS PEDIDOS)

def calcular_gasto(cliente_nome):
    for pedido in pedidos: # para cada dicionário na lista 'pedidos'
        if pedido["cliente"] == cliente_nome: # verifica se o nome do cliente corresponde
            total = sum(itens["preço"] for itens in pedido["itens"]) # soma os preços de todos os itens do cliente
            print(f"o valor total gasto por {cliente_nome} foi {total} R$")
        
calcular_gasto("Jhean")

# 2. Crie uma função que descubra qual prato foi o mais vendido no dia.

def mais_vendido():
    pratos_contagem = {} # cria um dicionario vazio chamado que será usado para armazenar o nome de cada prato como chave e a quantidade de vezes que ele foi pedido como valor
    for pedido in pedidos:
        for item in pedido["itens"]: # para cada item na lista de itens do pedido
            prato = item["prato"] # extrai o valor associado a chave "prato" de cada dicionario dentro da lista "itens" e armazena em uma variavel chamada 'prato' 
            pratos_contagem[prato] = pratos_contagem.get(prato, 0) + 1 # acessa ou inicializa a contagem do prato no dicionario "pratos_contagem", o método .get(prato, 0) retorna o valor atual da chave prato (se existir) ou 0 (se não existir) e soma 1 para incrementar a contagem de vezes que esse prato foi pedido
    var = max(pratos_contagem.items(), key=lambda x: x[1])[0] # usa a função max() para encontrar o par chave-valor (prato e sua contagem) com o maior valor (contagem). o argumento key=lambda[1] diz para ordenar com base no segundo elemento de cada par (a contagem). 0 [0] no final seleciona apenas a chave (o nome do prato) do par como maior contagem e a retorna
    print(f"o ptato mais vendido é: {var}")  
    # print(pratos_contagem)

mais_vendido()


# 3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente.

def ranking():
    gastos = {}
    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = sum(item["preço"] for item in pedido["itens"])
        gastos[cliente] = total

    var = sorted(gastos.items(), key=lambda x: x[1], reverse=True)[:3]
    print(var)
    print(gastos)

ranking()