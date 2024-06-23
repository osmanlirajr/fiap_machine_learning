from bs4 import BeautifulSoup
from modelos.vinho import Vinho 
import requests
import pandas as pd
import os

# Definir constantes para os tipos de produto
VINHO_DE_MESA = 'VINHO DE MESA'
VINHO_FINO_DE_MESA = 'VINHO FINO DE MESA (VINIFERA)'
SUCO = 'SUCO'
DERIVADOS = 'DERIVADOS'
class Producao:
    """
    Classe responsável por recuperar e processar dados de produção de vinhos.

    Métodos:
        recupera_producao(url: str) -> list[Vinhos]: Baixa e processa dados de produção a partir de um arquivo CSV.
    """
    @staticmethod
    def recupera_producao(url):
        """
        Baixa o arquivo CSV da URL fornecida, processa os dados e retorna uma lista de objetos Vinhos.

         Parâmetros:
            url (str): URL do arquivo CSV.

        Retorna:
            list[Vinhos]: Lista de objetos Vinhos contendo os dados processados.
        """
        temp_file_path = 'Producao_temp.csv'

        # Verificar se o arquivo temporário já existe e deletá-lo
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        # Fazer o download do arquivo CSV
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição

        # Salvar o conteúdo do CSV em um arquivo temporário
        with open(temp_file_path, 'wb') as file:
            file.write(response.content)
        print('salvei arquivo')
        # Carregar o arquivo CSV
        df = pd.read_csv(temp_file_path, delimiter=';')

        # Inicializar uma lista vazia para armazenar os resultados
        result_list = []

        # Iterar sobre cada linha no dataframe
        for index, row in df.iterrows():
            produto = row['produto']
            tipo_produto = row['control']
            
            # Ignorar linhas com tipo_produto começando com VINHO DE MESA, VINHO FINO DE MESA (VINIFERA), SUCO ou DERIVADOS
            if any(tipo_produto.startswith(prefix) for prefix in [VINHO_DE_MESA, VINHO_FINO_DE_MESA, SUCO, DERIVADOS]):
                continue
            
            # Ajustar tipo_produto conforme o prefixo
            if tipo_produto.startswith('vm_'):
                tipo_produto = VINHO_DE_MESA
            elif tipo_produto.startswith('vv_'):
                tipo_produto = VINHO_FINO_DE_MESA
            elif tipo_produto.startswith('su_'):
                tipo_produto = SUCO
            elif tipo_produto.startswith('de_'):
                tipo_produto = DERIVADOS
            
            # Iterar sobre cada coluna de ano (de 1970 a 2023)
            for year in range(1970, 2024):
                year_str = str(year)
                if year_str in row:
                    quantidade = row[year_str]
                    result_list.append(Vinho(produto, quantidade, tipo_produto, year))

        # Ordenar a lista pelo ano
        result_list_sorted = sorted(result_list, key=lambda x: x.ano)

        return result_list_sorted

