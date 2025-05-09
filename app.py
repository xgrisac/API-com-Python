# API - Local que disponibiliza recursos/funcionalplacaades
# 1 - OBJETIVO - Criar uma API que disponibiliza consulta, criação, edição e exclusão de estacionamento
# 2 - URL BASE - localhost.com
# 3 - ENDPOINT - GET, POST, PUT E DELETE
# 4 - RECURSOS - estacionamento

from flask import Flask, jsonify, request # jsonify é o formato de retorno da API e request acesso os dados que estão indo e vindo da requisção
from datetime import datetime

app = Flask(__name__)

# Lista de dicionários

estacionamento = [ 
    {
        'placa' : 'ABC1D23',
        'Modelo' : 'Fiat Palio',
        'Condutor' : 'João Silva',
        'entrada' : datetime.now().isoformat(),
        'saida' : None,
        'observacao': None
    },

    {
        'placa' : 'ABC1D23',
        'Modelo' : 'Volkswagem Gol',
        'Condutor' : 'Maria Oliveira',
        'entrada' : datetime.now().isoformat(),
        'saida' : None,
        'observacao': None
    },

    {
        'placa' : 'XYZ9K88',
        'Modelo' : 'Honda Xre',
        'Condutor' : 'Pedro Souza',
        'entrada' : datetime.now().isoformat(),
        'saida' : None,
        'observacao': None
    },
]

# Endpoint para consultar todos
@app.route('/estacionamento', methods=['GET']) # Detalhe que torna minha função um endpoint da API
def obter_estacionamento():
    return jsonify(estacionamento)

# Endpoint para consultar por placa
@app.route('/estacionamento/<placa>', methods=['GET']) # INT define que o valor que precisa retornar é inteiro e correspondente ao meu placa
def obter_estacionamento_por_placa(placa):
    for carro in estacionamento:
        if carro.get('placa') == placa: # Verifica se o placa atual é igual ao solicitado
            return jsonify(carro)

# Endpoint para edição por placa
@app.route('/estacionamento/<placa>', methods=['PUT'])
def editar_carro_por_placa(placa):
    carro_alterado = request.get_json() # Envia as informações do usuário para a API
    for indice,carro in enumerate(estacionamento):
        if carro.get('placa') == placa:
            estacionamento[indice].update(carro_alterado)
            return jsonify(estacionamento[indice])
        
# Endpoint para entrada de placa
@app.route('/estacionamento', methods=['POST'])
def criar_novo_carro():
    novo_carro = request.get_json()

    # Remove qualquer tentativa de enviar 'entrada' ou 'saida'
    novo_carro.pop('entrada', None)
    novo_carro.pop('saida', None)

    novo_carro['entrada'] = datetime.now().isoformat()
    novo_carro['saida'] = None

    estacionamento.append(novo_carro) #Append adciona 
    return jsonify(estacionamento)

# Endpoint para saída de placa
@app.route('/relatorio/<placa>', methods=['PUT'])
def registrar_saida(placa):
    carro_saida = request.get_json()  # Recebe as informações da requisição
    
    for carro in estacionamento:
        if carro.get('placa') == placa:
            if carro.get('saida') is not None:
                return jsonify({'mensagem': 'Saída já registrada anteriormente.'}), 400

            # Atribui a saída e a observação (caso fornecida)
            carro['saida'] = carro_saida.get('saida', None)  # Espera que a data/hora de saída seja fornecida
            carro['observacao'] = carro_saida.get('observacao', None)  # Se não enviar observação, permanece None
            return jsonify(carro)
    
    return jsonify({'erro': 'Carro não encontrado.'}), 404

# Endpoint para exclusão de placa
@app.route('/estacionamento/<placa>', methods=['DELETE'])
def deletar_carro(placa):
    for indice,carro in enumerate(estacionamento):
        if carro.get('placa') == placa:
            del estacionamento[indice] # Delete de acordo com o respectivo índice
            return jsonify(estacionamento)

import os

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

# http://localhost:5000/estacionamento link real de exibição no postman/navegador