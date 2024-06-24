class Importacao:
    """
    Classe que representa um registro de importação de vinho, uvas, espumantes e suco.

    Atributos:
        pais (str): Nome do pais.
        quantidade (int): Quantidade importada.
        valor (float): valor pela importação
        tipo_importacao (str): Tipo do produto (e.g., VINHO DE MESA, ESPUMANTES, UVAS FRESCAS, UVAS PASSAS, SUCO DE UVA).
        ano (int): Ano de importação.
    """
    def __init__(self, pais,quantidade, valor,tipo_importacao,ano):
        self._nome = pais
        self._quantidade = quantidade
        self._valor = valor
        self._tipo_importacao = tipo_importacao
        self._ano = ano