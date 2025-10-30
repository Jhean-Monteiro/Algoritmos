def busca_binaria_recursiva(lista, alvo, ini, fim):
    if ini > fim: # caso base: se os indices se cruzarem
        return - 1 # retorna - 1 se o alvo não for encontrado
    
    meio = (ini + fim) // 2
    if lista[meio] == alvo: 
        return meio
    
    elif lista[meio] < alvo: # se o elemento do meio for menor que o alvo
        '''print(ini, fim)'''
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim) # busca na metade direita

    else: # se o elemento do meio for maior que o alvo
        '''print(ini, fim)'''
        return busca_binaria_recursiva(lista, alvo, ini, meio - 1) # busca na metade esquerda
    


lista = []
for i in range(1, 300):
    lista.append(i)

alvo = 7
resultado = busca_binaria_recursiva(lista, alvo, 0, len(lista) - 1)
if resultado != -1:  # verifica se o resultado é válido
    print(f"Elemento {alvo} encontrado no índice {resultado}")  # exibe o índice
else:
    print(f"Elemento {alvo} não encontrado na lista")  # exibe mensagem de não encontrado