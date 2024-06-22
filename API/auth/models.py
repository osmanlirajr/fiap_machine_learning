from pydantic import BaseModel

class Token(BaseModel):
    """
    Modelo de dados para o token JWT.

    Atributos:
        access_token (str): Token de acesso.
        token_type (str): Tipo de token.
    """
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """
    Modelo de dados para o token JWT decodificado.

    Atributos:
        username (str | None): Nome de usuário contido no token.
    """
    username: str | None = None

class User(BaseModel):
    """
    Modelo de dados para o usuário.

    Atributos:
        username (str): Nome de usuário.
        email (str | None): Email do usuário.
        full_name (str | None): Nome completo do usuário.
        disabled (bool | None): Indica se o usuário está desativado.
    """
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    """
    Modelo de dados para o usuário no banco de dados.

    Atributos:
        hashed_password (str): Senha hash do usuário.
    """
    hashed_password: str