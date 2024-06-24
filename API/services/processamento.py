from bs4 import BeautifulSoup
from modelos.uvas import Uvas 
import requests
import pandas as pd
import os

# Definir constantes para os tipos de espécies de uvas
TINTAS = 'TINTAS'
BRANCAS_ROSADAS = 'BRANCAS E ROSADAS'

class Processamento:

    def recupera_processa(url, classificacao, temp_file_path):

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
            nome = str(row['cultivar']).strip()
            tipo = str(row['control']).strip()
            
            # Ignorar linhas com tipo_produto começando com VINHO DE MESA, VINHO FINO DE MESA (VINIFERA), SUCO ou DERIVADOS
            if any(tipo.startswith(prefix) for prefix in [TINTAS, BRANCAS_ROSADAS]):
                continue
            
            # Ajustar tipo_produto conforme o prefixo
            if tipo.startswith('ti_'):
                tipo = TINTAS
            elif tipo.startswith('br_'):
                tipo = BRANCAS_ROSADAS
            
            # Iterar sobre cada coluna de ano (de 1970 a 2023)
            for year in range(1970, 2024):
                year_str = str(year)
                if year_str in row:
                    quantidade = row[year_str]
                    result_list.append(Uvas(nome, quantidade, tipo, classificacao, year))

        # Deleta o arquivo temporário já existe e deletá-lo
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        # Ordenar a lista pelo ano
        result_list_sorted = sorted(result_list, key=lambda x: x.ano)

        return result_list_sorted

