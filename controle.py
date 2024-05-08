#https://github.com/rodrigo-labs/controle_estoque/blob/master/controle_de_estoque/controllers/controllers.py#L5

from Controle_de_login.cadastro import loginUsuario, loginAdmin


print("---Sistema de controle de estoque---\n")

login = input("---Identifique-se---\n1-Admin\n2-Usuário")

def loginMenu():
    opcao = login

    while True:
        if opcao == '1':
            loginUsuario()
        elif opcao == '2':
            loginAdmin()
        elif opcao =='0':
            return
        else:
            print("Entrada inválida", end="\n\n")


def loginUsuario(cadastro):
    usuario = input("Digite seu nome de usuário: ")

    while True:
        if (usuario == 'alvin'):
                senha = input("Senha: ")
                if senha == '1234':
                     print("Bem vindo!")                
        else:
            print("Usuário não existente!")   
            return loginUsuario() 
        

def loginAdmin():
    admin = input("Digite o login de administrador: ")

    while True:
        if (admin == 'admin'):
                senha = input("Senha: ")
                if senha == 'admin':
                     print("Bem vindo!")
                else:
                     print("Senha incorreta!")
                
        else:
            print("Login incorreto")
            return loginAdmin()


def menu_principal():

    while True:
        print("---------\n1-Cadastrar produto\n2-Lista de produtos\n3-Atualizar quantidade de produtos")
        opcao = input("Digite")

        if opcao == '1':
            cadastro_prod()
        elif opcao == '2':
            listar_prod()
        elif opcao == '3':
            atual_qunt()
        elif opcao == '0':
            sys.exit(0)
        else:
            print("OPÇÃO INVALIDA", end="\n\n")



def cadastro_prod():
    # produto1 = "Notebook positivo"
    # descr1 = "notebook positivo 8gb ram 128gb ssd"
    # cod1 = "1001"
    # produto2 = "Smartphone"
    # descr2 = "Celultar smartphone"
    # cod2 = "1002"

    opcao = cadastrar()
    produto = produto()
    descricao = descricao()
    codigo = int(codigo)

    while True:
        opcao = cadastrar.menu()
        
        if opcao == '1':
            try:
                produto = cadastrar.inserir()
                descricao = c
        nome = input("Digite o nome do produto: ")
        descprod = input("Digite a descrição do produto: ")
        codigo = input("Digite o codigo do produto: ")








    # username = input("Digite o nome de usuário: ")
    # if (username == Alvin) : 
    #     senha = input("Digite sua senha de usuário: ")
    # else: 
    #     print("Usuário não cadastrado!")
    #     return
    # if (senha == 12345):
    #     print(f"Bem vindo {username}.")
    # else: 
    #     print("Senha incorreta!")

    # Database.cursor.execute("""
    # SELECT * FROM Users
    # WHERE (User = ? and Password = ?)
    # """, (Username, Password))
    # VerifyLogin = Database.cursor.fetchone()
    # try: 
    #     if Username in VerifyLogin and Password in VerifyLogin:
    #         messagebox.showinfo(title="Login Info", message="Welcome! Access acept")
    # except:
    #     messagebox.showinfo(title="Login info", message="Access denied")
  