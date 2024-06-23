FIAP Machine Learning API
Esta é a API para o projeto de Machine Learning da FIAP, desenvolvida com Python e FastAPI.
Esta API pública de consulta nos dados do site http://vitibrasil.cnpuv.embrapa.br/index.php nas respectivas abas:

    Produção
    Processamento
    Comercialização
    Importação
    Exportação


Requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados em sua máquina:

Python 3.12
pip (gerenciador de pacotes do Python)
Instalação
Clone este repositório:

sh
Copiar código
git clone https://github.com/osmanlirajr/fiap_machine_learning.git
cd fiap_machine_learning/API
Crie um ambiente virtual:

sh
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:

sh
Copiar código
pip install -r requirements.txt
Executando a API
Certifique-se de que o ambiente virtual esteja ativado.

Execute o servidor FastAPI:

sh
Copiar código
uvicorn main:app --reload
Isso iniciará o servidor na porta 8000 por padrão. Você pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.

Estrutura do Projeto
main.py: Arquivo principal onde a aplicação FastAPI é configurada e iniciada.
modelos/: Contém os modelos de dados utilizados pela API.
negocios/: Contém  as classes de negocio da API.
auth/: contem as funcoes que prove a segurança da API com JWT.



