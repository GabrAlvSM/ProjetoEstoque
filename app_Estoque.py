from sys import exception


def iniciar(opcao):
    opcao = str(input("Bem vindo!\SnJá possui cadastro de usuário? S/N\n-"))

    if opcao == 'S':
        return usuario_logar(usuario_logar)
    elif opcao =='0':
        return fim()
    elif opcao == 'N':
        return cadastra_usuario(usuario_logar)
    else:
        print("Entrada inválida!", end="\n\n")


def fim():
    print("Encerrando....")
    return


def cadastra_usuario(novo):
    global novo_usuario
    global senha_n_usuario

    novo_usuario = input("Digite seu sobrenome e três ultimos digitos de telefone: ")
    senha_n_usuario = input("Digite uma senha: ")

    # novo = (novo_usuario, senha_n_usuario)

    print("Agora que possui cadastro por favor faça login\n")
    return usuario_logar(usuario_logar)


def usuario_logar(usuario):

    usuario = input("Digite seu nome de usuário: ")

    if (usuario == 'alvin'):
        senha = input("Senha: ")
        if senha == '1234':
            print(f"Bem vindo {usuario}!")
            return 
    elif (usuario == novo_usuario):
        senha = input("Digite sua senha: ")
        if (senha == senha_n_usuario):
            print(f"Bem vindo {novo_usuario}!")
            return exception
    elif (usuario != novo_usuario and usuario != 'alvin'):
        print("Usuário não existente!")
        return exception
    elif (usuario == '0'):
        fim()
    else:
        print("Usuário não existente!")
        return iniciar(iniciar)

