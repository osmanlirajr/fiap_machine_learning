from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from negocio.producao import Producao
from auth.security import SecurityConfig
from auth.models import Token
from auth.models import User
from auth.models import UserInDB
from auth.user_manager import UserManager
from auth.token_manager import TokenManager
from modelos.vinhos_response import VinhosResponse
import json

app = FastAPI()

# URL do CSV de producão
url = 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'

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


@app.get('/api/producao',response_model=list[VinhosResponse])
async def get_producao():
    """
    Endpoint da API que retorna dados de produção de vinhos no formato JSON.

    Retorna:
        list[VinhosResponse]: Lista de registros de produção de vinhos.
    """
    producao = Producao.recupera_producao(url)
    
    # Converter a lista de objetos para uma estrutura JSON
    producao_json = [vinho.__dict__ for vinho in producao]

    # Salvar o JSON em um arquivo
    with open('Producao_ordenada.json', 'w') as json_file:
        json.dump(producao_json, json_file, indent=4)

    return producao_json

@app.get('/api/processamento')
def get_processamento():
    return {}

@app.get('/api/comercializacao')
def get_comercializacao():
    return {}

@app.get('/api/importacao')
def get_importacao():
    return {}

@app.get('/api/exportacao')
def get_exportacao():
    return {}






