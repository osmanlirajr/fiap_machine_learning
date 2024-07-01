from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from services.producao import Producao
from services.processamento import Processamento
from services.comercializacao import Comercializacao
from services.exportacao import Exportacao
from services.importacao import Importacao
from auth.security import SecurityConfig
from auth.models import Token
from auth.models import User
from auth.models import UserInDB
from auth.user_manager import UserManager
from auth.token_manager import TokenManager
import json

app = FastAPI()

# URL do CSV de producão
urlProducao = 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
# URL do CSV de Comercializacao
urlComercializacao ='http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv'

# URL do CSV de processamento de Viniferas
urlProcessaViniferas = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv'

# URL do CSV de processamento de Americanas e Hibridas
urlProcessaAmericanas = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv'

# URL do CSV de processamento de Uvas de mesa
urlProcessaMesa = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv'

# URL do CSV de processamento de uvas sem classificacao
urlProcessaSemclass = 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv'

# URL do CSV de exportacao de vinhos de mesa
urlExportaVinho = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv'

# URL do CSV de exportacao de Espumantes
urlExportaEspumnante = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv'

# URL do CSV de exportacao de Uvas Frescas
urlExportaUvasFrescas = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv'

# URL do CSV de exportacao de Suco de Uvas
urlExportaSucoUvas = 'http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv'

# URL do CSV de importacao de vinhos de mesa
urlImportaVinho = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv'

# URL do CSV de importacao de Espumantes
urlImportaEspumnante = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv'

# URL do CSV de importacao de Uvas Frescas
urlImportaUvasFrescas = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv'

# URL do CSV de importacao de Uvas Passas
urlImportaUvasPassas = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv'

# URL do CSV de importacao de Suco de Uvas
urlImportaSucoUvas = 'http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv'



@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    """
    Autentica o usuário e retorna um token JWT.

    Args:
        form_data (OAuth2PasswordRequestForm): Formulário contendo as credenciais do usuário.

    Returns:
        Token: Token de acesso JWT.

    Raises:
        HTTPException: Se as credenciais forem inválidas.
    """
    user = UserManager.authenticate_user(UserManager.fake_user_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=SecurityConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = TokenManager.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Novos Endpoints com segurança
@app.get("/protected-route")
async def protected_route(payload: dict = Depends(TokenManager.verify_token)):
    return {"message": "Você tem acesso ao endpoint protegido", "payload": payload}


@app.get('/api/producao')
async def get_producao(payload: dict = Depends(TokenManager.verify_token)):
    """
    Endpoint da API que retorna dados de produção de vinhos no formato JSON.
    Endpoint protegido que só pode ser acessado com um token JWT válido.
    
    Args:
    payload (dict): Payload do token JWT decodificado.

    Retorna:
        list[Vinho]: Lista de registros de produção de vinhos.
    """
    producao = Producao.recupera_producao(urlProducao)
    
    # Converter a lista de objetos para uma estrutura JSON
    producao_json = [vinho.__dict__ for vinho in producao]

    # Salvar o JSON em um arquivo
    with open('Producao_ordenada.json', 'w') as json_file:
        json.dump(producao_json, json_file, indent=4)

    return producao_json

@app.get('/api/processamento')
async def get_processamento(payload: dict = Depends(TokenManager.verify_token)):
    """
    Endpoint da API que retorna dados de cultivo de uvas no formato JSON.
    Endpoint protegido que só pode ser acessado com um token JWT válido.
    
    Args:
    payload (dict): Payload do token JWT decodificado.

    Retorna:
        list[Uvas]: Lista de registros de uvas cultivadas.
    """
    processa_viniferas = Processamento.recupera_processamento(urlProcessaViniferas, 'VINIFERAS', 'Processa_Viniferas_temp.csv')
    processa_americanas = Processamento.recupera_processamento(urlProcessaAmericanas, 'AMERICANAS E HIBRIDAS', 'Processa_Americanas_temp.csv')
    processa_mesa = Processamento.recupera_processamento(urlProcessaMesa, 'UVAS DE MESA', 'Processa_Mesa_temp.csv')
    processa_semclass = Processamento.recupera_processamento(urlProcessaSemclass, 'SEM CLASSIFICACAO', 'Processa_Semclass_temp.csv')


    todas_uvas = processa_viniferas + processa_americanas + processa_mesa + processa_semclass

    # Converter a lista de objetos para uma estrutura JSON
    processa_json = [uvas.__dict__ for uvas in todas_uvas]

    #processa_json.append ([uvas.__dict__ for uvas in processa_americanas])
    # Salvar o JSON em um arquivo
    with open('Processamento_ordenado.json', 'w') as json_file:
        json.dump(processa_json, json_file, indent=4)


    return processa_json


@app.get('/api/comercializacao')
async def get_comercializacao(payload: dict = Depends(TokenManager.verify_token)):
    """
    Endpoint da API que retorna dados de comercialização de vinhos no formato JSON.
    Endpoint protegido que só pode ser acessado com um token JWT válido.
    
    Args:
    payload (dict): Payload do token JWT decodificado.

    Retorna:
        list[Vinho]: Lista de registros de comercialização de vinhos.
    """
    comercializacao = Comercializacao.recupera_comercializacao(urlComercializacao)
    
    # Converter a lista de objetos para uma estrutura JSON
    comercializacao_json = [vinho.__dict__ for vinho in comercializacao]

    # Salvar o JSON em um arquivo
    with open('Comercialicao_ordenada.json', 'w') as json_file:
        json.dump(comercializacao_json, json_file, indent=4)

    return comercializacao_json


@app.get('/api/importacao')
async def get_importacao(payload: dict = Depends(TokenManager.verify_token)):
    """
    Endpoint da API que retorna dados de exportação em JSON.
    Endpoint protegido que só pode ser acessado com um token JWT válido.
    
    Args:
    payload (dict): Payload do token JWT decodificado.

    Retorna:
        list[Exportacao]: Lista de registros de exportação.
    """
    
    importa_vinnhos = Importacao.recupera_importacao(urlExportaVinho, 'VINHOS DE MESA', 'Importa_Vinhos_temp.csv')
    importa_espumantes = Importacao.recupera_importacao(urlExportaEspumnante, 'ESPUMANTES', 'Importa_Espumantes_temp.csv')
    importa_uvas_frescas = Importacao.recupera_importacao(urlExportaUvasFrescas, 'UVAS FRESCAS', 'Importa_uvas_frescas_temp.csv')
    importa_uvas_passas = Importacao.recupera_importacao(urlExportaUvasFrescas, 'UVAS PASSAS', 'Importa_uva_passas_temp.csv')
    importaca_suco = Importacao.recupera_importacao(urlExportaSucoUvas, 'SUCO DE UVAS', 'Importa_suco_temp.csv')


    todas_importacoes = importa_vinnhos + importa_espumantes + importa_uvas_frescas + importa_uvas_passas + importaca_suco

    # Converter a lista de objetos para uma estrutura JSON
    processa_json = [importacao.__dict__ for importacao in todas_importacoes]

    
    # Salvar o JSON em um arquivo
    with open('importacao_ordenado.json', 'w') as json_file:
        json.dump(processa_json, json_file, indent=4)


    return processa_json


@app.get('/api/exportacao')
async def get_exportacao(payload: dict = Depends(TokenManager.verify_token)):
    """
    Endpoint da API que retorna dados de exportação em JSON.
    Endpoint protegido que só pode ser acessado com um token JWT válido.
    
    Args:
    payload (dict): Payload do token JWT decodificado.

    Retorna:
        list[Exportacao]: Lista de registros de exportação.
    """
    
    exporta_vinnhos = Exportacao.recupera_exportacao(urlExportaVinho, 'VINHOS DE MESA', 'Exporta_Vinhos_temp.csv')
    exporta_espumantes = Exportacao.recupera_exportacao(urlExportaEspumnante, 'ESPUMANTES', 'Exporta_Espumantes_temp.csv')
    exporta_uvas = Exportacao.recupera_exportacao(urlExportaUvasFrescas, 'UVAS FRESCAS', 'Expofrta_uvas_temp.csv')
    exporta_suco = Exportacao.recupera_exportacao(urlExportaSucoUvas, 'SUCO DE UVAS', 'exporta_suco_temp.csv')


    todas_exportacoes = exporta_vinnhos + exporta_espumantes + exporta_uvas + exporta_suco

    # Converter a lista de objetos para uma estrutura JSON
    processa_json = [exportacao.__dict__ for exportacao in todas_exportacoes]

    
    # Salvar o JSON em um arquivo
    with open('exportacao_ordenado.json', 'w') as json_file:
        json.dump(processa_json, json_file, indent=4)


    return processa_json





