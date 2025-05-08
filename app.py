# API - Local que disponibiliza recursos/funcionalplacaades
# 1 - OBJETIVO - Criar uma API que disponibiliza consulta, criação, edição e exclusão de carros
# 2 - URL BASE - localhost.com
# 3 - ENDPOINT - GET, POST, PUT E DELETE
# 4 - RECURSOS - carros

from flask import Flask, jsonify, request # jsonify é o formato de retorno da API e request acesso os dados que estão indo e vindo da requisção

app = Flask(__name__)

# Lista de dicionários

carros = [ 
    {
        'placa' : 'GXG7B73',
        'Modelo' : 'Fiat Palio',
        'Condutor' : 'Fulano de tal'
    },

    {
        'placa' : 'ABC1D23',
        'Modelo' : 'Volkswagem Gol',
        'Condutor' : 'Ciclano da Silva'
    },

    {
        'placa' : 'XYZ9K88',
        'Modelo' : 'Honda Xre',
        'Condutor' : 'Beltrano de Souza'
    },
]

# Endpoint para consultar todos
@app.route('/carros', methods=['GET']) # Detalhe que torna minha função um endpoint da API
def obter_carros():
    return jsonify(carros)

# Endpoint para consultar por placa
@app.route('/carros/<placa>', methods=['GET']) # INT define que o valor que precisa retornar é inteiro e correspondente ao meu placa
def obter_carros_por_placa(placa):
    for carro in carros:
        if carro.get('placa') == placa: # Verifica se o placa atual é igual ao solicitado
            return jsonify(carro)

# Endpoint para edição por placa
@app.route('/carros/<placa>', methods=['PUT'])
def editar_carro_por_placa(placa):
    carro_alterado = request.get_json() # Envia as informações do usuário para a API
    for indice,carro in enumerate(carros):
        if carro.get('placa') == placa:
            carros[indice].update(carro_alterado)
            return jsonify(carros[indice])
        
# Endpoint para criação
@app.route('/carros', methods=['POST'])
def criar_novo_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro) #Append adciona 
    return jsonify(carros)

# Endpoint para exclusão
@app.route('/carros/<placa>', methods=['DELETE'])
def deletar_carro(placa):
    for indice,carro in enumerate(carros):
        if carro.get('placa') == placa:
            del carros[indice] # Delete de acordo com o respectivo índice
            return jsonify(carros)

app.run(port=5000, host='localhost', debug=True)

# http://localhost:5000/carros link real de exibição no postman/navegador