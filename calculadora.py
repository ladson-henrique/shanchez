
opcao = ""
continuar_comprar = "sim"
print("Bem-vindos aos Restaurante pé d'aguan")
while continuar_comprar == "sim":
    opcao = ""
    print("A começar compra... \n")

    while opcao not in ['a', 'b', 'c', 'd']:

        print("Menu do Restaurante: \n")
        print("a) Bacalhau com  Natas")
        print("b) Frango Assado")
        print("c) Polvo")
        print("d) File com Fritas")
        print("\n")

        opcao = input("opcao -> ")
        print("\n")
        if opcao not in ['a', 'b', 'c', 'd']:
            print("opção invalida, tente novamente uma opção do nosso MENU \n")
        else:
            print("Adicionado " + opcao + " ao carrinho \n")

    continuar_comprar = input("Deseja continuar a compra ?  (sim/não): ").strip().lower()

print("Finalizando Pedido")
print("Finalizando Entrega")