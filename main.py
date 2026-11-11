
from Lanche import Lanche
from Bebida import Bebida
from Sobremesa import Sobremesa
from Gerenciador_Produtos import Gerenciador_Produtos


gerenciador = Gerenciador_Produtos()

while True:
    print("\n===== LANCHONETE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Preparar produtos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n1 - Lanche")
        print("2 - Bebida")
        print("3 - Sobremesa")

        tipo = input("Escolha o tipo de produto: ")

        if tipo not in ["1", "2", "3"]:
            print("Tipo inválido!")
            continue

        nome = input("Nome: ")

        try:
            preco = float(input("Preço: R$ "))
            estoque = int(input("Estoque: "))

            if tipo == "1":
                ingredientes = input("Ingredientes: ")

                produto = Lanche(
                    nome, preco, estoque, ingredientes
                )

            elif tipo == "2":
                tamanho = int(input("Tamanho em ml: "))

                produto = Bebida(
                    nome, preco, estoque, tamanho
                )

            elif tipo == "3":
                tipo_sobremesa = input("Tipo da sobremesa: ")

                produto = Sobremesa(
                    nome, preco, estoque, tipo_sobremesa
                )

            gerenciador.cadastrar(produto)

        except ValueError as erro:
            print("Erro:", erro)

    elif opcao == "2":
        gerenciador.listar()

    elif opcao == "3":
        nome = input("Digite o nome do produto: ")

        produto = gerenciador.buscar(nome)

        if produto:
            print(produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        gerenciador.executar_acao()

    elif opcao == "5":
        print("Obrigado por utilizar o sistema do Scooby Lanches!")
        break

    else:
        print("Opção inválida!")
