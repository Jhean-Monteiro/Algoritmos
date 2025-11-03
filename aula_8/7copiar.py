# Copiar o conteúdo de um arquivo para outro.

with open('texto.txt', 'r') as origem:
    with open('copia.txt', 'w') as destino:
        destino.write(origem.read())
print('conteúdo copiado para copia.txt!')