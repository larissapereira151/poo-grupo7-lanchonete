
from Produto import Produto


class Sobremesa(Produto):

    def __init__(self, nome, preco, estoque, tipo):
        super().__init__(nome, preco, estoque)
        self.tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("Tipo inválido.")
        self._tipo = valor

    def preparar(self):
        return f"Servindo a sobremesa {self.nome}."

    def mostrar_tipo(self):
        return f"Tipo: {self.tipo}"

    def __str__(self):
        return super().__str__() + f" | Tipo: {self.tipo}"
