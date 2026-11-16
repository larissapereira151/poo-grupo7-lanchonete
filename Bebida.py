
from Produto import Produto


class Bebida(Produto):

    def __init__(self, nome, preco, estoque, tamanho_ml):
        super().__init__(nome, preco, estoque)
        self.tamanho_ml = tamanho_ml

    @property
    def tamanho_ml(self):
        return self._tamanho_ml

    @tamanho_ml.setter
    def tamanho_ml(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Tamanho inválido.")
        self._tamanho_ml = valor

    def preparar(self):
        return f"Servindo a bebida {self.nome}."

    def mostrar_tamanho(self):
        return f"Tamanho: {self.tamanho_ml} ml"

    def __str__(self):
        return super().__str__() + f" | Tamanho: {self.tamanho_ml} ml"
