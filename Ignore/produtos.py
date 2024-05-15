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
