# API - Local que disponibiliza recursos/funcionalidades
# 1 - OBJETIVO - Criar uma API que disponibiliza consulta, criação, edição e exclusão de livros
# 2 - URL BASE - localhost.com
# 3 - ENDPOINT - GET, POST, PUT E DELETE
# 4 - RECURSOS - Livros

from flask import Flask, jsonify, request # jsonify é o formato de retorno da API e request acesso os dados que estão indo e vindo da requisção

app = Flask(__name__)

# Lista de dicionários

livros = [ 
    {
        'id' : 1,
        'titulo' : 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor' : 'J.R.R Tolkien'
    },

    {
        'id' : 2,
        'titulo' : 'Livro 2',
        'autor' : 'Autor 2'
    },

    {
        'id' : 3,
        'titulo' : 'Livro 3',
        'autor' : 'Autor 3'
    },
]

# Endpoint para consultar todos
@app.route('/livros', methods=['GET']) # Detalhe que torna minha função um endpoint da API
def obter_livros():
    return jsonify(livros)

# Endpoint para consultar por ID
@app.route('/livros/<int:id>', methods=['GET']) # INT define que o valor que precisa retornar é inteiro e correspondente ao meu ID
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id: # Verifica se o ID atual é igual ao solicitado
            return jsonify(livro)

# Endpoint para edição por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json() # Envia as informações do usuário para a API
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Endpoint para criação
@app.route('/livros', methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro) #Append adciona 
    return jsonify(livros)

# Endpoint para exclusão
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice] # Delete de acordo com o respectivo índice
            return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)

# http://localhost:5000/livros link real de exibição no postman/navegador