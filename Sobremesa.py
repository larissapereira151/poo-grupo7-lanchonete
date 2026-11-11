
from Produto import Produto


class Sobremesa(Produto):
    """Classe que representa as sobremesas."""

    def __init__(self, nome, preco, estoque, tipo):
        super().__init__(nome, preco, estoque)
        self.tipo = tipo

    @property
    def tipo(self):
        """Retorna o tipo da sobremesa."""
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        """Altera o tipo da sobremesa."""
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("Tipo inválido.")
        self._tipo = valor

    def preparar(self):
        """Serve uma sobremesa."""
        return f"Servindo a sobremesa {self.nome}."

    def mostrar_tipo(self):
        """Mostra o tipo da sobremesa."""
        return f"Tipo: {self.tipo}"

    def __str__(self):
        """Retorna os dados da sobremesa."""
        return super().__str__() + f" | Tipo: {self.tipo}"
