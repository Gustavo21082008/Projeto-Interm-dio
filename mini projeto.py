stock_total = ["arroz","feijão","Farofa"]
preço1 = ([15,14,10])
quantidade = (["Quantidade:35","Quantidade:40","Quantidade 100"])
carrinho_produtos = []
carrinnho_quantidade = []
def ver_stock():
 print("stock_total",stock_total,)
 print("preço",preço1)
 print("quantidade",quantidade)
def Comprar_Produto():
    print()

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