import csv
from fastapi import FastAPI #0.111.0
import requests #2.32.3
from bs4 import BeautifulSoup #0.0.2

app = FastAPI()

# Caminho para onde é exportado o csv
caminho = r"D:\Pós-Graduação\1 - Fase\2 - Pyton para ML e IA\Exercícios\Python\fastApiProject\\"

@app.get("/")
async def inicio():
    return "Seja bem-vindo"

@app.get("/prod")
async def produtos():
    all_dados_produtos = []

    # For para percorrer os anos no link
    for ano in range(1970, 2024):
        url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02'
        # Faz uma solicitação HTTP para obter o conteúdo da página
        response = requests.get(url)
        # Analisa o conteúdo HTML da página usando BeautifulSoup
        site = BeautifulSoup(response.text, "html.parser")
        # Encontra a tabela de produtos
        tabela_produtos = site.find("table", {"class": "tb_base tb_dados"})

        for linha in tabela_produtos.find_all("tr"):
            colunas = linha.find_all("td")
            # Quantidade de colunas da tabela
            if len(colunas) == 2:
                produto = colunas[0].text.strip()
                quantidade = colunas[1].text.strip()
                all_dados_produtos.append({"Ano": ano, "Produto": produto, "Quantidade": quantidade})

    # Escrita do arquivo csv no formato de encoding ANSI
    with open(caminho + "produtos.csv", mode='w', newline='', encoding='ANSI') as file:
        # Nome das colunas a serem gravadas no csv
        fieldnames = ["Ano", "Produto", "Quantidade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_dados_produtos:
            writer.writerow(item)

    return all_dados_produtos

@app.get("/proc")
async def processamento():
    all_dados_processamento = []

    for ano in range(1970, 2024):
        url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_01'
        response = requests.get(url)
        site = BeautifulSoup(response.text, "html.parser")
        tabela_produtos = site.find("table", {"class": "tb_base tb_dados"})
        for linha in tabela_produtos.find_all("tr"):
            colunas = linha.find_all("td")
            if len(colunas) == 2:
                cultivar = colunas[0].text.strip()
                quantidade = colunas[1].text.strip()
                all_dados_processamento.append({"Ano": ano, "Cultivo": cultivar, "Quantidade": quantidade})

    with open(caminho + "processamento.csv" , mode='w', newline='', encoding='ANSI') as file:
        fieldnames = ["Ano", "Cultivo", "Quantidade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_dados_processamento:
            writer.writerow(item)

    return all_dados_processamento

@app.get("/com")
async def comercializacao():
    all_dados_comercializacao = []

    for ano in range(1970, 2024):
        url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04'
        response = requests.get(url)
        site = BeautifulSoup(response.text, "html.parser")
        tabela_produtos = site.find("table", {"class": "tb_base tb_dados"})

        for linha in tabela_produtos.find_all("tr"):
            colunas = linha.find_all("td")
            if len(colunas) == 2:
                produto = colunas[0].text.strip()
                quantidade = colunas[1].text.strip()
                all_dados_comercializacao.append({"Ano": ano,"Produto": produto, "Quantidade": quantidade})

    with open(caminho + "comercializacao.csv", mode='w', newline='', encoding='ANSI') as file:
        fieldnames = ["Ano", "Produto", "Quantidade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_dados_comercializacao:
            writer.writerow(item)

    return all_dados_comercializacao

@app.get("/imp")
async def importacao():
    all_dados_importacao = []

    # URL do site que contém a tabela de produtos
    for ano in range(1970, 2024):
        url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_01'
        response = requests.get(url)
        site = BeautifulSoup(response.text, "html.parser")
        tabela_produtos = site.find("table", {"class": "tb_base tb_dados"})

        for linha in tabela_produtos.find_all("tr"):
            colunas = linha.find_all("td")
            if len(colunas) == 3:  # Assumindo que há tres colunas: país, quantidade, valor
                pais = colunas[0].text.strip()
                quantidade = colunas[1].text.strip()
                valor = colunas[2].text.strip()
                all_dados_importacao.append({"Ano": ano,"País": pais,"Quantidade": quantidade, "Valor": valor})

    with open(caminho + "importacao.csv", mode='w', newline='', encoding='ANSI') as file:
        fieldnames = ["Ano", "País", "Quantidade", "Valor"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_dados_importacao:
            writer.writerow(item)

    return all_dados_importacao

@app.get("/exp")
async def exportacao():
    all_dados_exportacao = []

    for ano in range(1970, 2024):
        url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_01'
        response = requests.get(url)
        site = BeautifulSoup(response.text, "html.parser")
        tabela_produtos = site.find("table", {"class": "tb_base tb_dados"})

        for linha in tabela_produtos.find_all("tr"):
            colunas = linha.find_all("td")
            if len(colunas) == 3:
                pais = colunas[0].text.strip()
                quantidade = colunas[1].text.strip()
                valor = colunas[2].text.strip()
                all_dados_exportacao.append({"Ano": ano,"País": pais,"Quantidade": quantidade, "Valor": valor})

    with open(caminho + "exportacao.csv", mode='w', newline='', encoding='ANSI') as file:
        fieldnames = ["Ano", "País", "Quantidade", "Valor"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_dados_exportacao:
            writer.writerow(item)

    return all_dados_exportacao