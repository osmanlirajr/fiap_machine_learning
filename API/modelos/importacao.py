class Importacao:
    """
    Classe que representa um registro de importação de vinho, uvas, espumantes e suco.

    Atributos:
        pais (str): Nome do pais.
        quantidade (str): Quantidade importada.
        tipo (str): Tipo do produto (e.g., VINHO DE MESA, ESPUMANTES, UVAS FRESCAS, UVAS PASSAS, SUCO DE UVA).
        ano (int): Ano de importação.
    """
    def __init__(self, pais, quantidade, tipo, ano):
        self.pais = pais
        self.quantidade = quantidade
        self.tipo = tipo
        self.ano = ano