from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from services.producao import Producao
from services.processamento import Processamento
from services.comercializacao import Comercializacao
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

# URL do CSV de processamento de Viniferas
urlProcessaViniferas = 'http://vitibrasil.cnpuv.embrapa.br/download/Processa_Viniferas.csv'

# URL do CSV de processamento de Americanas e Hibridas
urlProcessaAmericanas = 'http://vitibrasil.cnpuv.embrapa.br/download/Processa_Americanas.csv'

# URL do CSV de processamento de Uvas de mesa
urlProcessaMesa = 'http://vitibrasil.cnpuv.embrapa.br/download/Processa_Mesa.csv'

# URL do CSV de processamento de uvas sem classe
urlProcessaSemclass = 'http://vitibrasil.cnpuv.embrapa.br/download/Processa_Semclass.csv'

# URL do CSV de Comercializacao
urlComercializacao ='http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv'

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
        list[VinhosResponse]: Lista de registros de produção de vinhos.
    """
    producao = Producao.recupera_producao(urlProducao)
    
    # Converter a lista de objetos para uma estrutura JSON
    producao_json = [vinho.__dict__ for vinho in producao]

    # Salvar o JSON em um arquivo
    with open('Producao_ordenada.json', 'w') as json_file:
        json.dump(producao_json, json_file, indent=4)

    return producao_json

@app.get('/api/processamento')
async def get_processamento():
    
    processa_viniferas = Processamento.recupera_processa(urlProcessaViniferas, 'Viniferas', 'Processa_Viniferas_temp.csv')
    processa_americanas = Processamento.recupera_processa(urlProcessaAmericanas, 'Americanas e Hibridas', 'Processa_Americanas_temp.csv')
    processa_mesa = Processamento.recupera_processa(urlProcessaMesa, 'Uvas de Mesa', 'Processa_Mesa_temp.csv')
    processa_semclass = Processamento.recupera_processa(urlProcessaSemclass, 'Sem Classificacao', 'Processa_Semclass_temp.csv')


    todas_uvas = processa_viniferas + processa_americanas + processa_mesa + processa_semclass

    # Converter a lista de objetos para uma estrutura JSON
    processa_json = [uvas.__dict__ for uvas in todas_uvas]

    
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
        list[VinhosResponse]: Lista de registros de comercialização de vinhos.
    """
    comercializacao = Comercializacao.recupera_comercializacao(urlComercializacao)
    
    # Converter a lista de objetos para uma estrutura JSON
    comercializacao_json = [vinho.__dict__ for vinho in comercializacao]

    # Salvar o JSON em um arquivo
    with open('Comercialicao_ordenada.json', 'w') as json_file:
        json.dump(comercializacao_json, json_file, indent=4)

    return comercializacao_json


@app.get('/api/importacao')
async def get_importacao():
    return {}

@app.get('/api/exportacao')
async def get_exportacao():
    return {}






