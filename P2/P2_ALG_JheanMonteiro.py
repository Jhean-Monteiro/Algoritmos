# Implemente um programa para um museu de artes, visando atender tanto aos visitantes, 
# interessados em explorar as obras (presencialmente ou virtualmente), quanto aos 
# colaboradores, responsáveis pela gestão e manutenção do acervo. O museu abriga uma 
# variedade de obras de arte, representando artistas de diferentes períodos e estilos. Cada 
# obra possui informações detalhadas, como título, data de criação, tema, estilo artístico, 
# descrição, técnica utilizada, autor e localização na sala de exposição. Os artistas, por sua 
# vez, têm seus próprios perfis cadastrados, contendo nome, data e local de nascimento, 
# biografia e os estilos artísticos aos quais estão associados. Os estilos artísticos são 
# caracterizados por uma denominação, período de influência, descrição das características 
# predominantes e a principal escola representativa do estilo. Além disso, as obras de arte 
# podem ser acompanhadas por documentos relacionados, como cartas, fotografias ou 
# entrevistas. Em algumas ocasiões, uma obra retrata uma figura proeminente da época, 
# como nobres ou militares, sendo realizada uma pesquisa sobre a pessoa retratada e 
# cadastrada como parte das informações da obra. O museu também realiza empréstimos 
# de obras para eventos externos, registrando informações como período de empréstimo, 
# nome do evento, responsável e tema. Esse registro é essencial para manter o histórico dos 
# empréstimos e acompanhar as obras temporariamente fora do museu. Além disso, turistas 
# e escolas frequentemente solicitam visitas guiadas com roteiros específicos. Esses 
# roteiros incluem um tema, descrição e as obras a serem visitadas em sequência.


'''================================================================================================================================'''

# No programa é preciso conter 
# 1. Funções 

import random
def aleatorio(): # vai ser usado mais pra frente
    lista = []
    for i in range(1, 20):
        aleatorio = random.randint(1,20)
        lista.append(aleatorio)
    return lista


'''================================================================================================================================'''

# 2. Utilização de listas 
'ps: na 3 eu já usei logo uma lista de dicionários, mas vou fazer uma outra lista aqui também só por garantia ._.'
artistas = ['João', 'Maria', 'Pedro', 'Lucas', 'Leonardo']

# 3. Utilização de dicionários 
'ps: não sei nada de arte, então inventei as coisas aqui ._.'

obras = [ 
    {
        "titulo": "Joãozinho", 
        "data": 1500, 
        "tema": "infantil", 
        "estilo": "desenho"
     },
    {
        "titulo": "Mariazinha", 
        "data": 1501, 
        "tema": "infantil", 
        "estilo": "desenho"
        },
    {
        "titulo": "Pedrão", 
        "data": 1700, 
        "tema": "terror", 
        "estilo": "escultura"}
] # isso aqui só vai ser implementado lá na questão 7

# print(obras)

# listas = { 
#     {"titulos": ["Joãozinho", "Mariazinha", "Pedrinho"]},
#     {"datas": [1500, 1501, 1700]},
#     {"temas": ["infantil", "infantil", "terror"]},
#     {"estilos":["desenho", "desenho", "escultura"]}
# }


# print(listas)



'''================================================================================================================================'''

# 4. A utilização de um Algoritmo de Ordenação, ficando a seu critério a escolha  

'ps: estudei muito isso aqui ._.'
def quickSort(lista):
    if len(lista)<=1:
        return lista
    
    pivo = lista[-1]
    esquerda = []
    direita = []

    for i in lista[:-1]:
        if i < pivo:
            esquerda.append(i)

        else:
            direita.append(i)

    return quickSort(esquerda) + [pivo] + quickSort(direita)

# teste
print("\nPS: toda vez que rodar o código, a funçao aleatorio() vai gerar uma lista diferente")
lista_desordenada = aleatorio()
print(f"a lista desordenada é: {lista_desordenada}")
lista_ordenada = quickSort(lista_desordenada)
print(f"lista ordenada (pós QuickSort): {lista_ordenada}") # funciona!



'''================================================================================================================================'''

# 5. Implemente um algoritmo de Busca  

'ps: estudei bastante essa também'
def BuscaBin(lista,alvo): # busca binária
    ini = 0
    fim = len(lista) -1

    while ini<=fim:
        meio = (ini+fim)//2
        if lista[meio] == alvo:
            return meio
        
        elif lista[meio] > alvo:
            fim = meio-1

        else:
            ini = meio+1

    return "não encontrado" # se o loop while acabar sem retornar nada, é porque o alvo não foi achado

# teste
lista_ordenada = quickSort(lista_desordenada)
numero = 6
teste = BuscaBin(lista_ordenada, numero) # funciona só com listas ordenadas
print(f"\n(ordenada): numero {numero} no indice: {teste}") # funciona



def BuscaSeq(lista, alvo): # busca sequencial
    for indice, valor in enumerate(lista):
        if valor == alvo:
            return indice
    return "não encontrado"

# teste
teste2 = BuscaSeq(lista_desordenada, numero) # teste com lista desordenada

print(f"(desordenada): numero {numero} no indice: {teste2}") # funciona


'''================================================================================================================================'''

# 6. Uso de Arquivos (podendo ser leitura ou escrita)  
'ps: não sei o que fazer. não estudei nem um pouco disso aqui. foi mal ._.'


'''================================================================================================================================'''

# 7. Deve considerar possíveis exceções 




try:
    entrada = int(input("\n0 = Joãozinho \n1 = Mariazinha \n2 = Pedrão \nescolha uma obra de arte para ver com a família!: "))
    if entrada in [2]:
        print("obra de terror! entrada apenas para adultos! apenas para adultos!")
        
    elif entrada in [0, 1]:
        print("obra infantil! entrada livre")


    else:
        print("digite numeros entre 0 e 2!")

except ValueError:
    print("digite números!")
    
# finally:
#     print("aproveite!")



# aplicação parecida com a de cima, mas sem try e except:

# for obra in obras:
#     if obra["tema"] == "terror":
#          print("obra de terror! entrada apenas para adultos! apenas para adultos!")
        
#     else:
#         print("obra infantil! entrada livre")



