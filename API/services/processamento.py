from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Definir constantes para os tipos de espécies de uvas
TINTAS = 'TINTAS'
BRANCAS_ROSADAS = 'BRANCAS E ROSADAS'

class Processamento:

    def recupera_processa_viniferas(url):

        temp_file_path = 'Processa_Viniferas_temp.csv'

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