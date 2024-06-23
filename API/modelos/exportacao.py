class Exportacao:
    """
    Classe que representa um registro de exposrtacao de vinho, uvas, espumantes e suco.

    Atributos:
        pais (str): Nome do pais.
        quantidade (int): Quantidade exposrtada.
        valor (float): valor exportado
        tipo_exportacao (str): Tipo do produto (e.g., VINHO DE MESA, ESPUMANTES, UVAS FRESCAS, SUCO DE UVA).
        ano (int): Ano de exportacao.
    """
    def __init__(self, pais,quantidade, valor,tipo_exportacao,ano):
        self._nome = pais
        self._quantidade = quantidade
        self._valor = valor
        self._tipo_exportacao = tipo_exportacao
        self._ano = ano