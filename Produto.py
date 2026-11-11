
class Produto:
    "Classe base dos produtos da lanchonete."

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    # Getter e setter do nome
    @property
    def nome(self):
        "Retorna o nome do produto."
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Altera o nome do produto."""
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("Nome inválido.")
        self.__nome = valor

    # Getter e setter do preço
    @property
    def preco(self):
        """Retorna o preço do produto."""
        return self.__preco

    @preco.setter
    def preco(self, valor):
        """Altera o preço do produto."""
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("Preço inválido.")
        self.__preco = valor

    # Getter e setter do estoque
    @property
    def estoque(self):
        """Retorna a quantidade em estoque."""
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        """Altera a quantidade em estoque."""
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Estoque inválido.")
        self.__estoque = valor

    def preparar(self):
        """Ação padrão do produto."""
        return "Preparando produto..."

    def __str__(self):
        """Retorna os dados do produto."""
        return f"Nome: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.estoque}"
