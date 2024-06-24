from typing import Union
from .models import UserInDB



class UserManager:
    """
    Classe para gerenciar usuários.

    Atributos:
        fake_user_db (dict): Banco de dados falso de usuários.
    """
    fake_user_db = {
        "user@example.com": {
            "username": "user",
            "full_name": "Fake User",
            "email": "user@example.com",
            "hashed_password": "fakehashedpassword",
            "disabled": False,
        }
    }

    @staticmethod
    def verify_password(fake_hashed_password: str, password: str) -> bool:
        """
        Verifica se a senha fornecida corresponde à senha hash falsa.

        Args:
            fake_hashed_password (str): Senha hash armazenada.
            password (str): Senha fornecida pelo usuário.

        Returns:
            bool: True se a senha for válida, False caso contrário.
        """
        return fake_hashed_password == password

    @staticmethod
    def get_user(db: dict, username: str) -> Union[UserInDB, None]:
        """
        Busca um usuário no banco de dados falso pelo nome de usuário.

        Args:
            db (dict): Banco de dados de usuários falsos.
            username (str): Nome de usuário.

        Returns:
            Union[UserInDB, None]: Objeto UserInDB se o usuário for encontrado, None caso contrário.
        """
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)

    @staticmethod
    def authenticate_user(fake_db: dict, username: str, password: str) -> Union[UserInDB, bool]:
        """
        Autentica o usuário verificando as credenciais.

        Args:
            fake_db (dict): Banco de dados de usuários falsos.
            username (str): Nome de usuário.
            password (str): Senha fornecida pelo usuário.

        Returns:
            Union[UserInDB, bool]: Objeto UserInDB se as credenciais forem válidas, False caso contrário.
        """
        user = UserManager.get_user(fake_db, username)
        if not user:
            return False
        if not UserManager.verify_password(user.hashed_password, password):
            return False
        return user