from pydantic import BaseModel

class VinhosResponse(BaseModel):
    """
    Modelo de resposta para a API de produção de vinhos.

    Atributos:
        produto (str): Nome do produto.
        quantidade (int): Quantidade produzida.
        tipo_produto (str): Tipo do produto.
        ano (int): Ano de produção.
    """
    produto: str
    quantidade: int
    tipo_produto: str
    ano: int