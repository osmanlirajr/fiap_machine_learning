from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
import jwt
from .security import SecurityConfig
from .models import TokenData, User, UserInDB
from .user_manager import UserManager

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenManager:
    """
    Classe para gerenciar tokens JWT.
    """

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        """
        Cria um token de acesso JWT com tempo de expiração.

        Args:
            data (dict): Dados a serem codificados no token.
            expires_delta (timedelta | None): Tempo de expiração do token.

        Returns:
            str: Token JWT codificado.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SecurityConfig.SECRET_KEY, algorithm=SecurityConfig.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        """
        Função para verificar e decodificar um token JWT.
        
        Args:
        credentials (HTTPAuthorizationCredentials): Credenciais de autorização.
        
        Returns:
        dict: Payload decodificado do token JWT.
        
        Raises:
        HTTPException: Exceção levantada se o token for inválido.
        """
        try:
            payload = jwt.decode(credentials.credentials, SecurityConfig.SECRET_KEY, algorithms=[SecurityConfig.ALGORITHM])
            return payload
        except jwt.PyJWTError:
            raise HTTPException(status_code=403, detail="Credenciais inválidas")

