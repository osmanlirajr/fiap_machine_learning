API está usando FAST API.

Para facilitar a configuração usamos o Ambientes Virtuais em Python com venv.
A venv é uma biblioteca integrada ao Python 3.3 e versões posteriores, enquanto virtualenv é uma ferramenta externa que precisa ser instalada separadamente. Para versões mais recentes do Python (3.5 e acima), venv é recomendada, pois oferece funcionalidades semelhantes às do virtualenv e está disponível de forma padrão.


O Ven ja está configurado neste projeto. Precisamos apenas ativar o ambiente virtual antesrodar a API. Para isso, execute o seguinte commando:

MAc e Linux
    source venv/bin/activate

Windows
    venv/Scripts/activate.bat


Para subir o projeto da API executa o seguinte comando no terminal:
- uvicorn main:app --reload

Para chamar os metodos REST

http://127.0.0.1:8080/api/NOMEDOREST

Para chamar a Documentação da API

http://127.0.0.1:8080/docs


