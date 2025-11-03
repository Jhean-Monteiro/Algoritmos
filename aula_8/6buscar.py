# Buscar uma palavra em um arquivo e exibir as linhas onde ela aparece.


palavra = 'novo'
with open('texto.txt', 'r') as file:
    for numero, linha in enumerate(file, 1):
        if palavra in linha.lower():
            print(f'linha {numero}: {linha.strip()}')