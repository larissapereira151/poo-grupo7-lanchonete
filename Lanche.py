
from Produto import Produto


class Lanche(Produto):
    """Classe que representa os lanches."""

    def __init__(self, nome, preco, estoque, ingredientes):
        super().__init__(nome, preco, estoque)
        self.ingredientes = ingredientes

    @property
    def ingredientes(self):
        """Retorna os ingredientes."""
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, valor):
        """Altera os ingredientes."""
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("Ingredientes inválidos.")
        self._ingredientes = valor

    def preparar(self):
        """Prepara um lanche."""
        return f"Preparando o lanche {self.nome}."

    def mostrar_ingredientes(self):
        """Mostra os ingredientes do lanche."""
        return f"Ingredientes: {self.ingredientes}"

    def __str__(self):
        """Retorna os dados do lanche."""
        return super().__str__() + f" | Ingredientes: {self.ingredientes}"
