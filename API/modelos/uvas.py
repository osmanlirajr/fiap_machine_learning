class Uva:
    """
    Classe que representa um de uvas

    Atributos:
        nome (str): Nome da uva.
        quantidade (int): Quantidade 
        tipo (str): Tipo do uva (TINTAS, BRANCAS E ROSADAS).
        classificacao (str): Classificacao da Uva (VINIFERAS, AMERICANAS E HIBRIDAS, UVAS DE MESA, SEM CLASSFICACAO). 
        ano (int): Ano de importação.
    """
    def __init__(self, nome, quantidade,tipo, classificacao, ano):
        self.nome = nome
        self.quantidade = quantidade
        self.tipo = tipo
        self.classificacao = classificacao
        self.ano = ano
