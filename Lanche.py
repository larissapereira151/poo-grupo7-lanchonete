
from Produto import Produto


class Lanche(Produto):

    def __init__(self, nome, preco, estoque, ingredientes):
        super().__init__(nome, preco, estoque)
        self.ingredientes = ingredientes

    @property
    def ingredientes(self):
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("Ingredientes inválidos.")
        self._ingredientes = valor

    def preparar(self):
        return f"\nPREPARANDO O LANCHE 1{self.nome}.\nAguarde alguns minutos!"

    def mostrar_ingredientes(self):
        return f"Ingredientes: {self.ingredientes}"

    def __str__(self):
        return super().__str__() + f" | Ingredientes: {self.ingredientes}"
