# Contar o número de linhas em um arquivo.


with open('texto.txt', 'r') as file:
    linhas = file.readlines()
    print(f'número de linhas: {len(linhas)}')