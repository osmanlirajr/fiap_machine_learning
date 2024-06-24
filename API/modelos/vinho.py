class Vinho:
    """
    Classe que representa um registro de produção de vinho.

    Atributos:
        produto (str): Nome do produto.
        quantidade (int): Quantidade produzida.
        tipo_produto (str): Tipo do produto (e.g., VINHO DE MESA, VINHO FINO DE MESA).
        ano (int): Ano de produção.
    """
    def __init__(self, produto, quantidade, tipo_produto, ano):
        self.produto = produto
        self.quantidade = quantidade
        self.tipo_produto = tipo_produto
        self.ano = ano