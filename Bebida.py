
from Produto import Produto


class Bebida(Produto):
    """Classe que representa as bebidas."""

    def __init__(self, nome, preco, estoque, tamanho_ml):
        super().__init__(nome, preco, estoque)
        self.tamanho_ml = tamanho_ml

    @property
    def tamanho_ml(self):
        """Retorna o tamanho da bebida."""
        return self._tamanho_ml

    @tamanho_ml.setter
    def tamanho_ml(self, valor):
        """Altera o tamanho da bebida."""
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Tamanho inválido.")
        self._tamanho_ml = valor

    def preparar(self):
        """Serve uma bebida."""
        return f"Servindo a bebida {self.nome}."

    def mostrar_tamanho(self):
        """Mostra o tamanho da bebida."""
        return f"Tamanho: {self.tamanho_ml} ml"

    def __str__(self):
        """Retorna os dados da bebida."""
        return super().__str__() + f" | Tamanho: {self.tamanho_ml} ml"
