import pandas as pd
import requests
from io import StringIO

class Exportacao:
    """
    Classe responsável por recuperar e processar dados de exportação.

    Métodos:
        recupera_exportacao(url: str, tipo_produto: str) -> list[list]: Baixa e processa dados de exportação a partir de um arquivo CSV.
    """
    @staticmethod
    def recupera_exportacao(url, tipo_produto):
        """
        Baixa o arquivo CSV da URL fornecida, processa os dados e retorna uma lista de listas com os dados transformados.

         Parâmetros:
            url (str): URL do arquivo CSV.
            tipo_produto (str): Tipo de produto para adicionar como coluna no DataFrame.

        Retorna:
            list[list]: Lista de listas contendo os dados transformados.
        """
        # Fazer a requisição do arquivo CSV da URL fornecida
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        response.encoding = 'utf-8'  # Define a codificação do response para UTF-8

        # Carregar o CSV em memória usando StringIO
        csv_data = StringIO(response.text)
        temp_dataframe = pd.read_csv(csv_data, sep=';')

        def transform_data(temp_dataframe, tipo_produto):
            """
            Transforma o DataFrame original em um novo DataFrame com colunas 'PAIS', 'ANO', 'QTD_KG', 'VALOR' e 'TIPO_PRODUTO'.

            Parâmetros:
                temp_dataframe (DataFrame): DataFrame original a ser transformado.
                tipo_produto (str): Tipo de produto para adicionar como coluna no DataFrame.

            Retorna:
                DataFrame: Novo DataFrame com a estrutura transformada.
            """
            country_col = temp_dataframe.pop('País')  # Remove a coluna 'País' do DataFrame original
            
            # Inicializa um dicionário para armazenar os dados transformados
            transform_dataframe = {
                'PAIS': [],
                'ANO': [],
                'QTD_KG': [],
                'VALOR': [],
                'TIPO_PRODUTO': []
            }
            
            # Itera sobre cada linha do DataFrame original
            for index, row in temp_dataframe.iterrows():
                for col in temp_dataframe.columns:
                    if col.endswith('.1'):  # Verifica se a coluna termina com '.1' indicando colunas de valor
                        year = col[:-2]  # Remove o '.1' para obter o ano
                        qtd_kg = temp_dataframe[year][index] if pd.notnull(temp_dataframe[year][index]) else 0
                        valor = row[col] if pd.notnull(row[col]) else 0
                        transform_dataframe['PAIS'].append(country_col[index])
                        transform_dataframe['ANO'].append(year)
                        transform_dataframe['QTD_KG'].append(qtd_kg)
                        transform_dataframe['VALOR'].append(valor)
                        transform_dataframe['TIPO_PRODUTO'].append(tipo_produto)
            
            return pd.DataFrame(transform_dataframe)

        # Transformar o DataFrame original
        transform_dataframe = transform_data(temp_dataframe, tipo_produto)
        return transform_dataframe.values.tolist()  # Converter o DataFrame transformado em uma lista de listas