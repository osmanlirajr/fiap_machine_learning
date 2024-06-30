from bs4 import BeautifulSoup
from modelos.uva import Uva 
import requests
import pandas as pd
import os

# Definir constantes para os tipos de espécies de uvas
TINTAS = 'TINTAS'
BRANCAS_ROSADAS = 'BRANCAS E ROSADAS'

class Processamento:
    """
    Classe responsável por recuperar e processar dados de cultivo de uvas.

    Métodos:
        recupera_processamento(url: str,classificacao: str, tem_file_path: str) -> list[Uvas]: Baixa e processa dados de cultivo de uvas a partir de um arquivo CSV.
    """
    @staticmethod
    def recupera_processamento(url, classificacao, temp_file_path):
        """
        Baixa o arquivo CSV da URL fornecida, processa os dados e retorna uma lista de objetos Uvas produzidas.

         Parâmetros:
            url (str): URL do arquivo CSV.
            classificacao (str): A Classificacao da Uva.
            temp_fileP_path (str): O nome do arquivos csv temporário. 

        Retorna:
            list[Uva]: Lista de objetos Uvas contendo os dados processados.
        """
        # Fazer o download do arquivo CSV
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição

        # Salvar o conteúdo do CSV em um arquivo temporário
        with open(temp_file_path, 'wb') as file:
            file.write(response.content)
        
        # Carregar o arquivo CSV
        if (str(temp_file_path).startswith('Processa_Americanas_')):
            df = pd.read_csv(temp_file_path, delimiter='\t')
        elif (str(temp_file_path).startswith('Processa_Mesa_')):
            df = pd.read_csv(temp_file_path, delimiter='\t')
        elif (str(temp_file_path).startswith('Processa_Semclass_')):
            df = pd.read_csv(temp_file_path, delimiter='\t')
        else :
           df = pd.read_csv(temp_file_path, delimiter=';') 
            

        # Inicializar uma lista vazia para armazenar os resultados
        result_list = []

        # Iterar sobre cada linha no dataframe
        for index, row in df.iterrows():
            nome = row['cultivar']
            tipo = row['control']
            
            # Ignorar linhas com tipo_produto começando com TINTAS, BRANCAS E ROSADAS
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
                    quantidade = str(row[year_str])
                    result_list.append(Uva(nome, quantidade, tipo, classificacao, year))

        # Deleta o arquivo temporário já existe e deletá-lo
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        # Ordenar a lista pelo anoi
        result_list_sorted = sorted(result_list, key=lambda x: x.ano) 

        return result_list_sorted