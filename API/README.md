
# FIAP Machine Learning API

Esta é a API para o projeto de Machine Learning da FIAP, desenvolvida com Python e FastAPI.
Esta API pública de consulta nos dados do site [Vitibrasil Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php) nas respectivas abas:

- Produção
- Processamento
- Comercialização
- Importação
- Exportação

## Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados em sua máquina:

- Python 3.12+
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/osmanlirajr/fiap_machine_learning.git
   cd fiap_machine_learning/API

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\bin\activate.bat`


3. Instale as dependências:
    ```sh
    pip install -r requirements.txt

## Testar a API localmente

1. Certifique-se de que o ambiente virtual esteja ativado.
2. Execute o servidor FastAPI:
     ```sh
     uvicorn main:app --reload

Isso iniciará o servidor na porta 8000 por padrão. Você pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.

## Estrutura do Projeto

-  main.py: Arquivo principal onde a aplicação FastAPI é configurada e iniciada.
-  modelos/: Contém os modelos de dados utilizados pela API.
-  services/: Contém Lógica de negócios e funções de serviço.
-  auth/: Contém as funções que provê a segurança da API com JWT.

## Teste

- Obtenha o Token JWT através do endpoint /token. (username:user@example.com / password:fakehashedpassword)
- Autentique-se no Swagger UI usando o botão "Authorize" e colocando bearer gerando no endpoint token.
- Teste os endpoints protegidos no Swagger UI, agora que você está autenticado.





