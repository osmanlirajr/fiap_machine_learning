O PROBLEMA
Você foi contratado para uma consultoria e seu trabalho envolve analisar dados de vitinicultura da Embrapa, os quais estão disponíveis aqui:
A ideia do projeto é a criação de uma API pública de consulta nos dados do site nas respectivas abas:

Produção
Processamento
Comercialização
Importação
Exportação
A API vai servir para alimentar uma base de dados que futuramente será usada para um modelo de Machine Learning.
Seus objetivos incluem:
Criar uma Rest API em Python que faça a consulta no site da Embrapa.
Sua API deve estar documentada.
é recomendável a escolha de um método de autenticação (JWT, por exemplo)
Criar um plano para fazer o deploy da API, desenhando a arquitetura de projeto desde a ingestão até a alimentação do modelo (aqui é necessário elaborar um modelo de ML, mas é preciso que vocês escolham um cenário interessante em que a API possa ser utilizada.)
Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.

—

ETAPAS
Coleta de dados - baixar dados em csv
Configurar ambiente de desenvolvimento - Flask ou FastAPI pra criar API Rest
Implementar os endpoints da API para consultar os dados do site da Embrapa.
Adicione a autenticação JWT (https://pyjwt.readt
