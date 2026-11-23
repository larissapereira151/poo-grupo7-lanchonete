
class Produto:

#INICIA
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

#ENCAPSULAMENTO
    # Getter e setter do nome
    @property
    def nome(self):
        return self.__nome

#CONTROLAR A ALTERAÇÃO DO NOME
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("Nome inválido.")
        self.__nome = valor

#PERMITE ACESSAR O PREÇO
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("Preço inválido.")
        self.__preco = valor

    # Getter e setter do estoque
    @property
    def estoque(self):
        return self.__estoque
#VEREFICA SE É UM NUM. INTEIRO OU NEGATIVO
    @estoque.setter
    def estoque(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Estoque inválido.")
        self.__estoque = valor

    def preparar(self):
        return "Preparando produto..."

    def __str__(self):
        return f"Nome: {self.nome} | Preço: R$ {self.preco:.2f} | Estoque: {self.estoque}"
