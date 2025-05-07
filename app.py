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

@ap.route('/livros') # Detalhe que torna minha função uma API
def obter_livros():
    return jsonify(livros)