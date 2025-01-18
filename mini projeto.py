produtos = ["arroz", "feijão", "farofa"]
preço1 = [15, 14, 10]
Quantidade = [35, 40, 100]
carrinho_produtos = []
carrinho_quantidade = []


def ver_stock():
    print("produtos", produtos, )
    print("preço", preço1)
    print("quantidade", Quantidade)


def Comprar_Produto():
    produto = input("Qual produto deseja adicionar ao carrinho? ").lower()
    if produto not in produtos:
        print("Esse produto não existe.")
    else:
        indice = produtos.index(produto)
        quantidade = int(input("Quantos produtos deseja adicionar? "))

        if quantidade > Quantidade[indice]:
            print("Quantidade insuficiente no estoque!")
        else:
            if produto not in carrinho_produtos:
                carrinho_produtos.append(produto)
                carrinho_quantidade.append(quantidade)
            else:
                carrinho_quantidade[carrinho_produtos.index(produto)] += quantidade
            Quantidade[indice] -= quantidade
            print(f"{quantidade} unidade(s) de {produto} adicionada(s) ao carrinho.")


def Remover_do_carrinho():
    produto = input("qual produto deseja remover do carrinho")
    if produto not in carrinho_produtos:
        print("Produto não está no carrinho")
    else:
        indice = carrinho_produtos.index(produto)
        quantidade = int(input(f"Quantas unidades de {produto} deseja remover"))
        if quantidade > carrinho_quantidade[indice]:
            print("Quantidade maior presente doque no carrinho")
        else:
            carrinho_quantidade[indice] -= quantidade
            if carrinho_quantidade[indice] == 0:
                carrinho_produtos.remove(produtos)
                carrinho_quantidade.remove(0)
            print(f"{quantidade}unidade(s) de {produto} removida(s) do carrinho")


def Finalizar_Compra():
    total = 0
    for i in range (len(carrinho_produtos)):
        indice = produtos.index(carrinho_produtos[i])
        total += preço1[indice] * carrinho_quantidade[i]
        print(f"total da compra: R${total:.2f}")
        print("Compra finalizada")


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
