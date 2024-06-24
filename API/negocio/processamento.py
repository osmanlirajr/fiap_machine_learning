import requests #2.32.3
from bs4 import BeautifulSoup #0.0.2

class Processamento:


    def recupera_processamento_viniferas(self):
        #Viníferas
        all_dados_processamento = []

        # For para percorrer os anos no link
        for ano in range(1970, 2024):
            
            url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02'
            # Faz uma solicitação HTTP para obter o conteúdo da página
            response = requests.get(url)
            # Analisa o conteúdo HTML da página usando BeautifulSoup
            site = BeautifulSoup(response.text, "html.parser")
            # Encontra a tabela de produtos
            tabela_processamento = site.find("table", {"class": "tb_base tb_dados"})

            for linha in tabela_processamento.find_all("tr"):
                colunas = linha.find_all("td")
                # Quantidade de colunas da tabela
                if len(colunas) == 2:
                    produto = colunas[0].text.strip()
                    if produto != 'VINHO DE MESA' or produto != 'VINHO FINO DE MESA (VINIFERA)'  or produto != 'SUCO ' or produto != 'DERIVADOS':
                        print(produto)
                        quantidade = colunas[1].text.strip()
                        all_dados_processamento.append({"Ano": ano, "Produto": produto, "Quantidade": quantidade})

        return all_dados_processamento

    def recupera_processamento_americanas_hibridas(self):
        #Americanas e híbridas

    
    def recupera_processamento_uvas_mesa(self):
        #Uvas de mesa

    def recupera_processamento_sem_classificacao(self):
        #Sem classificação