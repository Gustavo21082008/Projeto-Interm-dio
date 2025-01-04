stock_total = ["arroz","feijão","Farofa"]
preço1 = ([15,14,10])
Quantidade = (["Quantidade:35","Quantidade:40","Quantidade 100"])
carrinho_produtos = []
carrinho_quantidade = []
def ver_stock():
 print("stock_total",stock_total,)
 print("preço",preço1)
 print("quantidade",Quantidade)
def Comprar_Produto():
    produto = input("qual produto deseja adicionar ao carrinho")
    if produto not in stock_total:
        print("esse produto não existe")
    else:
        indice = produto.index(produto)
        if produto not in carrinho_produtos:
         (carrinho_produtos.append(produto))
    quantidade = int(input("quantos produtos deseja adicionar"))
    if quantidade > Quantidade[indice]:
        print("quantidade insuficiente no stock total!")
        carrinho_quantidade.append(Quantidade)

        stock_total[indice] -= quantidade
        print("produto adicionado com sucesso")
    else:
        carrinho_quantidade[indice] += quantidade

def Remover_do_carrinho():
    print("")


def Finalizar_Compra():
    print("")

def Adicionar_Estoque():
    print("")
while True:
    print(" 1.ver stock")
    print(" 2. Comprar Produto")
    print(" 3. Remover do Carrinho")
    print(" 4. Finalizar Compra")
    print(" 5. Adicionar Estoque")
    print(" 6. Sair")
    escolha = int(input("escolha uma opção"))
    if escolha == 1:
        ver_stock()
    elif escolha == 2:
        Comprar_Produto()
    elif escolha == 3:
        Remover_do_carrinho()
    elif escolha == 4:
        Finalizar_Compra()
    elif escolha == 5:
        Adicionar_Estoque()
    elif escolha == 6:
        break
    else:
     print("Opção invalidá")