import pandas as pd
import requests
from modelos.exportacao import Exportacao
import os

class Exportacao:
    """
    Classe responsável por recuperar e processar dados de exportação.

    Métodos:
        recupera_exportacao(url: str,classificacao: str, tem_file_path: str) -> list[list]: Baixa e processa dados de exportação a partir de um arquivo CSV.
    """
    def recupera_exportacao(url, classificacao, temp_file_path):
        """
        Baixa o arquivo CSV da URL fornecida, processa os dados e retorna uma lista de objetos Exportações produzidos.

         Parâmetros:
            url (str): URL do arquivo CSV.

        Retorna:
            list[Exportacao]: Lista de objetos Exporta;cão contendo os dados processados.
        """
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
        # Iterar sobre cada linha no dataframe
        for index, row in df.iterrows():
            pais = str(row['País']).strip()     
            # Iterar sobre cada coluna de ano (de 1970 a 2023)
            for year in range(1970, 2024):
                year_str = str(year)
                if year_str in row:
                    quantidade = str(row[year_str])
                    #result_list.append(Exportacao(pais, quantidade,classificacao, year))
                    result_list.append({'pais':pais,'quantidade': quantidade,'tipo_exportacao': classificacao,'ano': year})

        # Deleta o arquivo temporário já existe e deletá-lo
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        # Ordenar a lista pelo ano
        #result_list_sorted = sorted(result_list, key=lambda x: x.ano)

        return result_list
