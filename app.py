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

# Requisição consultar todos
@app.route('/livros', methods=['GET']) # Detalhe que torna minha função um endpoint da API
def obter_livros():
    return jsonify(livros)

# Requisição para consultar por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id: # Verifica se o ID atual é igual ao solicitado
            return jsonify(livro)

# Requisição para edição
@app.route('/livros/<int>:id', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json() # Retorna as informações do usuário para a API
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livro[indice])
        


app.run(port=5000, host='localhost', debug=True)

# http://localhost:5000/livros link real de exibição no postman/navegador