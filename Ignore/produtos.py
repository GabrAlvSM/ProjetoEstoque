def preencher(produtos):
    global lista_produtos

    nomep = "Nome: "
    descp = "Descrição"
    cod = "Cod: "
    qntp =  "Quantidade disponível: "

    produto1 = [f"{nomep}Smartphone Motorola \n{descp}Motorola moto edging 02 8gb, 258gb armazenamento \n{cod}2 \n {qntp}30"]
    produto2 = [f"{nomep}Notebook positivo \n{descp}notebook positivo 8gb ram 128gb ssd \n{cod} 3 \n {qntp}20"]

    produtos = print(produto1 + "\n" + produto2)

    lista_produtos = produtos




#     # produto1 = "Notebook positivo"
#     # descr1 = "notebook positivo 8gb ram 128gb ssd"
#     # cod1 = "1001"
#     # produto2 = "Smartphone"
#     # descr2 = "Celultar smartphone"
#     # cod2 = "1002"

# preencher(preencher)




####  Função que corre toda a lista 'thislist' ####

# thislist = ["apple", "banana", "cherry", "peach"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

#### Adicionar produto SUBSTITUIDO

# nomeprod = str(input("Digite o nome do produto: "))
# descprod = str(input("Digite a descrição do produto: "))
# codigoprod = int(input("Digite o codigo do produto: "))
# quantprod = int(input("Digite a quantidade de produtos distponíveis: ")) 

# produto = print(f"\nNome: {nomeprod} \nCod: {codigoprod} \nDescrição: {descprod} \nQuantidade disponível: {quantprod}\n")


#### editar e adicionar(incompleto) lista de produtos

    
# editar = input("Deseja editar os itens da lista? S/N\n-")

# if(editar == 'S'):
#     opt = int(input(f"Qual item deseja editar?\n Quantidade de itens editáveis: {i}\n-"))

#     opt = opt - 1

#     nome_edit = input("Digite o nome do produto: ")
#     desc_edit = input("Digite a descrição do produto: ")
#     qnt_edit = input("Informe a quantidade disponível de produtos: ")

#     list_produtos[opt] = nome_edit
#     list_descprods[opt] = desc_edit
#     list_quantprods[opt] = qnt_edit

# elif(editar == '2'):
#     opt = int(input(f"Qual item deseja editar?\n Quantidade de itens editáveis: {i}\n-"))

#     opt = opt - 1

#     nome_nov = input("Digite o nome do produto: ")
#     desc_novo = input("Digite a descrição do produto: ")
#     qnt_novo = input("Informe a quantidade disponível de produtos: ")

#     list_produtos.insert(1, nome_nov)
#     list_descprods.insert(1, desc_novo)
#     list_quantprods.insert(1, qnt_novo)


# else: 
#     print("Ok\nRetornando para o menu...")
#     pass