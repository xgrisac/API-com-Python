# API de Controle de Estacionamento com Flask 🚗

Este projeto consiste em uma API RESTful para gerenciamento de veículos em um estacionamento. A aplicação foi construída com Flask e permite a realização de operações CRUD (Create, Read, Update, Delete) para registrar a entrada e saída de veículos, além de permitir a inclusão de observações no momento da saída.

# Funcionalidades

Cadastro de veículos (POST): Registra a entrada de veículos com informações como placa, modelo, condutor, data de entrada e observação (opcional).

Consulta de veículos (GET): Permite consultar todos os veículos ou buscar informações de um veículo específico pelo número da placa.

Edição de informações de veículos (PUT): Permite editar dados como modelo ou condutor de um veículo registrado.

Exclusão de veículos (DELETE): Remove um veículo do sistema.

Registro de saída (PUT): Atualiza a data de saída do veículo, além de permitir a inclusão de observações sobre a saída.

# Tecnologias Utilizadas

. Python: Linguagem de programação principal.

. Flask: Framework utilizado para criação da API RESTful.

. Dicionários Python: Simulação de banco de dados utilizando listas e dicionários.

. Postman: Ferramenta utilizada para testar e verificar a funcionalidade da API.

. Render: Plataforma de deploy para hospedar a API e disponibilizá-la publicamente.

# Endpoints da API

1. Cadastro de Veículo

Método: POST

Endpoint: /estacionamento


2. Consultar Todos os Veículos

Método: GET

Endpoint: /estacionamento

3. Consultar Veículo por Placa

Método: GET

Endpoint: /estacionamento/{placa}

4. Editar Dados de um Veículo

Método: PUT

Endpoint: /estacionamento/{placa}

5. Registro de Saída

Método: PUT

Endpoint: /relatorio/{placa}

6. Excluir Veículo

Método: DELETE

Endpoint: /estacionamento/{placa}

# Como Rodar o Projeto Localmente

Clone o repositório:

bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git

Instale as dependências:

pip install -r requirements.txt

Inicie o servidor Flask:

python app.py

A API estará disponível em http://127.0.0.1:5000.

# Como Testar a API

Você pode testar os endpoints da API utilizando o Postman ou qualquer outra ferramenta que envie requisições HTTP.

# Exemplo de requisição POST para criar um novo veículo:

URL: http://127.0.0.1:5000/estacionamento

Método: POST

Corpo da Requisição Raw + (JSON):

json

Digite:

{
    "placa": "ABC1234",
    "Modelo": "Fiat Uno",
    "Condutor": "Maria Souza"
}


# Contribuições

Sinta-se à vontade para contribuir com melhorias, correções ou sugestões! Faça um fork deste repositório, crie uma branch, implemente as mudanças e envie um pull request.

# Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Deploy: https://api-para-controle-de-estacionamento-com.onrender.com/estacionamento / https://api-para-controle-de-estacionamento-com.onrender.com (A API está hospedada no Render)

![API PYTHON+FLASK](https://github.com/user-attachments/assets/fee39a11-1767-41f5-aa1d-7969361e8b86)

