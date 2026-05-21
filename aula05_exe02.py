def mostrar_menu():
    print("""
            ______JOGOS______
            |               |
            | 1- GTA VI  -> R$ 350
            | 2- FIFA 26 -> R$ 300
            | 3- FORZA 6 -> R$ 250
            |_______________|
    """)


def sistema():

    jogos = {
        "1": ("GTA VI", 350),
        "2": ("FIFA 26", 300),
        "3": ("FORZA 6", 250)
    }

    carrinho = []
    total = 0

    mostrar_menu()

    quantidade = int(input("Quantos jogos deseja comprar? (1 a 3): "))

    if quantidade < 1 or quantidade > 3:
        print("Quantidade inválida!")
        return

    for i in range(quantidade):

        opcao = input(f"Escolha o {i+1}º jogo: ")

        if opcao in jogos:
            nome, preco = jogos[opcao]

            carrinho.append(nome)
            total += preco

            print(f"{nome} adicionado ao carrinho!")
        else:
            print("Opção inválida!")

    print("\n===== RESUMO DA COMPRA =====")

    for jogo in carrinho:
        print(f"- {jogo}")

    print(f"\nTotal da compra: R$ {total:.2f}")


sistema()