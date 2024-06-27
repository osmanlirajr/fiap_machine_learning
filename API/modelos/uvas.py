class Uvas:
    """
    Classe que representa um de uvas

    Atributos:
        pais (str): Nome da uva.
        quantidade (int): Quantidade 
        tipo (str): Tipo do uva (TINTAS, BRANCAS E ROSADAS).
        classificacao (str): Classificacao da Uva (VINIFERAS, AMERICANAS E HIBRIDAS, UVAS DE MESA, SEM CLASSFICACAO).
        
        ano (int): Ano de importação.
    """
    def __init__(self, nome, quantidade,tipo, classificacao, ano):
        self._nome = nome
        self._quantidade = quantidade
        self._tipo = tipo
        self._classificacao = classificacao
        self._ano = ano
