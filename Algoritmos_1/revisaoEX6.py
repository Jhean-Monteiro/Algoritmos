# 2. Validação de Login 
# Implemente um algoritmo que simule um sistema de login: 
# • O usuário tem 3 tentativas para digitar a senha correta (senha123). 
# • Caso erre todas, mostre "Acesso bloqueado". 
# • Caso acerte, mostre "Bem-vindo!".

tentativas = 0

while True:
    entrada = input('insira a senha para entrar: ')
    tentativas = tentativas + 1

    if entrada in ['senha123', 'Gioliano melhor professor', 'me aprove pfv Gioliano']:
        print('senha correta! acesso permitido!')
        break

    elif tentativas == 3:
        print('tentativas excedidas. acesso bloqueado')
        break

    else:
        print('senha incorreta. tente novamente.')