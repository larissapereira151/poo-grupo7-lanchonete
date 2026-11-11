
class Gerenciador_Produtos:
    """Gerencia os produtos da lanchonete."""

    def __init__(self):
        """Cria a lista de produtos."""
        self._produtos = []

    def cadastrar(self, produto):
        """Adiciona um produto à lista."""
        self._produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    def listar(self):
        """Mostra todos os produtos cadastrados."""
        if len(self._produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self._produtos:
                print(produto)

    def buscar(self, nome):
        """Busca um produto pelo nome."""
        for produto in self._produtos:
            if produto.nome.lower() == nome.lower():
                return produto

        return None

    def executar_acao(self):
        """Executa o método preparar de todos os produtos."""
        if len(self._produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self._produtos:
                print(produto.preparar())

    def __str__(self):
        """Retorna a quantidade de produtos cadastrados."""
        return f"Total de produtos: {len(self._produtos)}"
