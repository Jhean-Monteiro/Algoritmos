def busca_binaria_validada(lista, alvo):
    if not lista:
        return - 1
    
    if not all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1)):
        raise ValueError("A lista deve estar ordenada!")
    
    ini = 0
    fim = len(lista) - 1

    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == alvo:
            return meio
        
        elif lista[meio] < alvo:
            # print(ini)
            ini = meio + 1

        else:
            # print(fim)
            fim = meio - 1

    return -1 # returna -1 se o alvo não for encontrado


lista_ord = []
for i in range(1,100000):
    lista_ord.append(i)

alvo = int(input("insira um numero: "))
try:
    resultado = busca_binaria_validada(lista_ord, alvo)
    if resultado != -1:
        print(f"Elemento {alvo} encontrado no indice {resultado}")

    else:
        print(f"Elemento {alvo} não encontrado na lista")

except ValueError as e:
    print(f"Erro: {e}")