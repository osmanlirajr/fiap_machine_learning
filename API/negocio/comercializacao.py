from bs4 import BeautifulSoup
from modelos.vinho import Vinho 
import requests
import pandas as pd
import os

# Definir constantes para os tipos de produto
VINHO_DE_MESA = 'VINHO DE MESA'
VINHO_FINO_DE_MESA = 'VINHO  FINO DE MESA'
VINHO_ESPECIAL = 'VINHO ESPECIAL'
SUCO = 'SUCO DE UVAS'
ESPUMANTES = 'ESPUMANTES'
OUTROS_PRODUTOS_COMERCIALIZADOS = 'OUTROS PRODUTOS COMERCIALIZADOS'
VINHO_FRIZANTE = 'VINHO FRIZANTE'
VINHO_ORGANICO = 'VINHO ORGÂNICO'
SUCO_DE_UVAS_CONCENTRADO = 'SUCO DE UVAS CONCENTRADO'

class Comercializacao:
    """
    Classe responsável por recuperar e processar dados de comercializacao de vinhos.

    Métodos:
        recupera_comercializacao(url: str) -> list[Vinhos]: Baixa e processa dados de comercializacao a partir de um arquivo CSV.
    """
    @staticmethod
    def recupera_comercializacao(url):
        """
        Baixa o arquivo CSV da URL fornecida, processa os dados e retorna uma lista de objetos Vinhos.

         Parâmetros:
            url (str): URL do arquivo CSV.

        Retorna:
            list[Vinhos]: Lista de objetos Vinhos contendo os dados comercializacao.
        """
        temp_file_path = 'Comercializacao_temp.csv'

        # Verificar se o arquivo temporário já existe e deletá-lo
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        # Fazer o download do arquivo CSV
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição

        # Salvar o conteúdo do CSV em um arquivo temporário
        with open(temp_file_path, 'wb') as file:
            file.write(response.content)
        # Carregar o arquivo CSV
        df = pd.read_csv(temp_file_path, delimiter=';')

        # Inicializar uma lista vazia para armazenar os resultados
        result_list = []
        tipo_produto_final= ''
        # Iterar sobre cada linha no dataframe
        for index, row in df.iterrows():
            produto = str(row['Produto']).strip()
            tipo_produto = str(row['control']).strip()
            
            # Ignorar linhas com tipo_produto 
            if any(tipo_produto.startswith(prefix) for prefix in [VINHO_DE_MESA,VINHO_ESPECIAL,ESPUMANTES, VINHO_FINO_DE_MESA, SUCO,OUTROS_PRODUTOS_COMERCIALIZADOS]):
                tipo_produto_final= tipo_produto
                continue
            
            # Ajustar tipo_produto conforme o prefixo para as execões
            if tipo_produto.startswith(VINHO_ORGANICO):
                tipo_produto_final =VINHO_ORGANICO
            elif tipo_produto.startswith(VINHO_FRIZANTE):
                tipo_produto_final = VINHO_FRIZANTE
            elif tipo_produto.startswith(SUCO_DE_UVAS_CONCENTRADO):
                tipo_produto_final = SUCO_DE_UVAS_CONCENTRADO
            elif tipo_produto.startswith('ou'):
                 tipo_produto_final = OUTROS_PRODUTOS_COMERCIALIZADOS           

            # Iterar sobre cada coluna de ano (de 1970 a 2023)
            for year in range(1970, 2024):
                year_str = str(year)
                if year_str in row:
                    quantidade = row[year_str]
                    result_list.append(Vinho(produto, quantidade, tipo_produto_final, year))

        # Ordenar a lista pelo ano
        result_list_sorted = sorted(result_list, key=lambda x: x.ano)

        return result_list_sorted

