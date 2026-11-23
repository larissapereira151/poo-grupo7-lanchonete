#gerencia os produtos, permitindo cadastrar, listar, buscar e executar ações.
class Gerenciador_Produtos:

    def __init__(self):
        self._produtos = []

#append(): adiciona um item ao final da lista.
    def cadastrar(self, produto):
        self._produtos.append(produto)
        print("Produto cadastrado com sucesso! 🌟")

    def listar(self):
        if len(self._produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self._produtos:
                print(produto)

    def buscar(self, nome):
        for produto in self._produtos:
            if produto.nome.lower() == nome.lower():
                return produto

        return None

    def executar_acao(self):
        if len(self._produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self._produtos:
                print(produto.preparar())

    def __str__(self):
        return f"Total de produtos: {len(self._produtos)}"
