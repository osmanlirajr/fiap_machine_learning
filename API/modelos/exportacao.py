class Exportacao:
    """
    Classe que representa um registro de exportação de vinho, uvas, espumantes e suco.

    Atributos:
        pais (str): Nome do pais.
        quantidade (int): Quantidade exportada.
        tipo (str): Tipo do produto (e.g., VINHO DE MESA, ESPUMANTES, UVAS FRESCAS, SUCO DE UVA).
        ano (int): Ano de exportação.
    """
    def __init__(self, pais, quantidade, tipo, ano):
        self.pais = pais
        self.quantidade = quantidade
        self.tipo = tipo
        self.ano = ano