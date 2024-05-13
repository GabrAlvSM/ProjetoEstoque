from sys import exception

def iniciar(opcao):
    opcao = str(input("Bem vindo!\nJá possui cadastro de usuário? S/N\n-"))

    if opcao == 'S':
        return usuario_logar(usuario_logar)
    
    elif opcao == 'N':
        print("Por favor faça login como Administrador para cadastrar um novo usuário!")
        return usuario_logar(usuario_logar)
    
    elif opcao =='0':
        return fim()
    
    else:
        print("Entrada inválida!", end="\n\n")

iniciar(iniciar)

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
    return usuario_logar(usuario='')


def usuario_logar(usuario):

    usuario = input("\nDigite seu nome de usuário: ")

    if (usuario == 'alvin'):
        senha = input("Senha: ")
        if senha == '1234':
            print(f"\nBem vindo {usuario}!")
            return menu_prod(menu_prod)
        
    elif (usuario == 'Admin'):
        senha = input("Senha: ")
        if senha == 'admin':
            print(f"\nBem vindo {usuario}!")
            return menuAdm(menuAdm)
        
    elif (usuario == novo_usuario):
        senha = input("Digite sua senha: ")
        if (senha == senha_n_usuario):
            print(f"Bem vindo {novo_usuario}!")
            return exception
        
    elif (usuario != novo_usuario and usuario != 'alvin' and usuario != 'Admin'):
        print("Usuário não existente!")
        return exception
    
    elif (usuario == '0'):
        fim()

    else:
        print("Usuário não existente!")
        return iniciar(iniciar)
    

def menu_prod(opcao):

    print("\nDigite a opção desejada:\n")
    opcao = input("1 - Ver lista de produtos \n2 - Cadastar um novo produto\n-")

    list_produtos = ["Monitor LG", "Smartphone Samsung S23", "Cabo Cat5 10m"]
    list_descprods = ["Monitor LG 144Hz", "Smartphone S23 Camera de 50Mp, 8gm RAM, 256Gb Armazenamento ", "Cabo de rede Cat5 com 10 metros de comprimento"]
    list_quantprods = [50, 100, 70]

    while(True):

        produto = ''


        if opcao == '2':

            nomeprod = str(input("Digite o nome do produto: "))
            descprod = str(input("Digite a descrição do produto: "))
            codigoprod = int(input("Digite o codigo do produto: "))
            quantprod = int(input("Digite a quantidade de produtos distponíveis: ")) 
            
            produto = [nomeprod, descprod, codigoprod, quantprod]
        
            #produto = [nomeprod, descprod, codigoprod, quantprod] #print(f"\n\nProduto adicionado: {nomeprod}\nDescrição: {descprod}\nCód: {codigoprod} \nQuantidade em estoque: {quantprod}")

            return menu_prod(menu_prod)
        

        ####  Função que corre toda a lista 'thislist' ####

        # thislist = ["apple", "banana", "cherry", "peach"]
        # i = 0
        # while i < len(thislist):
        #     print(thislist[i])
        #     i = i + 1


        if opcao == '1':
            if(produto == ''):

                print("\nLista de produtos:\n")
                i=0
                while i < len(list_produtos):
                    print(f"Nome: {list_produtos[i]} \nDescrição: {list_descprods[i]} \nQuantidade disponível: {list_quantprods[i]}\n")
                    i = i + 1
  
                # print("Nenhum produto registrado!")

                print(produto)
                return menu_prod(opcao='')
            else:
                print(produto)
                return menu_prod(opcao='')
    

            



def menuAdm(opcao):
    
    print("\n---Bem vindo ao menu de administração---\n\nDigite a opção desejada:")
    opcao = input("1-Cadastrar novo login\n2-Menu padrão\n-")

    if opcao == '1':
        return cadastra_usuario(cadastra_usuario)
    
    elif opcao == '2':
        return menu_prod(menu_prod)
    
