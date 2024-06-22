class SecurityConfig:
    """
    Configuração de segurança para a aplicação.
    
    Atributos:
        SECRET_KEY (str): Chave secreta para codificação JWT.
        ALGORITHM (str): Algoritmo de codificação JWT.
        ACCESS_TOKEN_EXPIRE_MINUTES (int): Tempo de expiração do token em minutos.
    """
    SECRET_KEY = "Minha_chave"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30