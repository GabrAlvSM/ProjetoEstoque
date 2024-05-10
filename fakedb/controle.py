# #https://github.com/rodrigo-labs/controle_estoque/blob/master/controle_de_estoque/controllers/controllers.py#L5

# import array
# from hmac import new
# import string
# from fakedb import produtos

# def fim():
#     print("Encerrando....")
#     return


# def iniciar(opcao):
#     opcao = input("---Identifique-se---\n1-Admin\n2-Usuário\n-")

#     if opcao == '1':
#         loginAdmin(loginAdmin)
#     elif opcao == '2':
#         loginUsuario(loginUsuario)
#     elif opcao =='0':
#         fim()
#     else:
#         print("Entrada inválida!", end="\n\n")


# def loginUsuario(usuario):
#     usuario = input("Digite seu nome de usuário: ")

#     while True:
#         if (usuario == 'alvin'):
#                 senha = input("Senha: ")
#                 if senha == '1234':
#                     print("Bem vindo!")
#                     return menu_principal(menu_principal)
#         elif (usuario == '0'):
#             fim()
#         else:
#             print("Usuário não existente!")        


# def loginAdmin(admin):
#     admin = input("Digite o login de administrador: ")

#     while True:
#         if (admin == 'admin'):
#                 senha = input("Senha: ")
#                 if senha == 'admin':
#                     print("Bem vindo!")
#                     return menu_principal(menu_principal)
#                 else:
#                     print("Senha incorreta!")
                
#         else:
#             print("Login incorreto!")


# def menu_principal():

#     while True:
#         print("---------\n1-Cadastrar produto\n2-Lista de produtos\n3-Atualizar quantidade de produtos")
#         opcao = input("Digite")

#         if opcao == '1':
#             cadastro_prod()
#         elif opcao == '2':
#             listar_prod()
#         elif opcao == '3':
#             atual_qunt()
#         elif opcao == '0':
#             fim()
#         else:
#             print("OPÇÃO INVALIDA", end="\n\n")



# def cadastro_prod(produto):

#     nomeprod = input("Digite o nome do produto: ")
#     descprod = input("Digite a descrição do produto: ")
#     codigoprod = input("Digite o codigo do produto: ")

#     lista_prods = []

#     list.produto = produto(nomeprod, descprod, codigoprod)

# def listar_prod(lista):
    

#     print(array.produtos, array.produto)
#     lista = print(produtos, cadastro_prod(produto=string))





#     # username = input("Digite o nome de usuário: ")
#     # if (username == Alvin) : 
#     #     senha = input("Digite sua senha de usuário: ")
#     # else: 
#     #     print("Usuário não cadastrado!")
#     #     return
#     # if (senha == 12345):
#     #     print(f"Bem vindo {username}.")
#     # else: 
#     #     print("Senha incorreta!")

#     # Database.cursor.execute("""
#     # SELECT * FROM Users
#     # WHERE (User = ? and Password = ?)
#     # """, (Username, Password))
#     # VerifyLogin = Database.cursor.fetchone()
#     # try: 
#     #     if Username in VerifyLogin and Password in VerifyLogin:
#     #         messagebox.showinfo(title="Login Info", message="Welcome! Access acept")
#     # except:
#     #     messagebox.showinfo(title="Login info", message="Access denied")
