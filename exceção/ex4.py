# 4.Exceções personalizadas: Escreva uma função que verifica se uma senha possui no mínimo 8 caracteres e pelo menos um número. Se a senha não atender aos requisitos, levante uma exceção com uma mensagem personalizada. Trate a exceção e mostre a mensagem ao usuário.


try:
    senha = input("Digite sua senha: ")

    if len(senha) < 8:
        print("Erro: A senha deve ter no mínimo 8 caracteres.")

    else:
        tem_numero = False
        for caractere in senha: # percorre cada digito na senha
            if caractere.isdigit(): # verifica se algum digite é decimal
                tem_numero = True
                break
        
        if not tem_numero:
            print("Erro: A senha deve conter pelo menos um número.")

        else:
            print("Senha válida!")

except:
    print("Erro: Entrada inválida. Digite uma senha válida.")


finally:
    print("Verificação de senha encerrada.")